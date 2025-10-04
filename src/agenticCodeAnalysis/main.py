import os
import json
from crewai import Crew, Task, Process

from src.agenticCodeAnalysis.config.Agents import create_code_analysis_agents
from src.agenticCodeAnalysis.config.InitializationAgent import get_architect
from src.agenticCodeAnalysis.config.Manager import create_manager_agent
from src.agenticCodeAnalysis.config.Tasks import create_code_analysis_tasks
from src.agenticCodeAnalysis.config.Tools import *
from src.agenticCodeAnalysis.llms.gemini import gemini
from src.agenticCodeAnalysis.llms.local import local_llm

# --- Configuration ---
# Set your project and output directories
# NOTE: Update these paths to be correct for your execution environment
PROJECT_DIRECTORY = '/mnt/85e3eeea-3bda-4255-95a1-833fffd20e34/dev/Agentic-Experiments/temp/spring-boot-ecommerce'
OUTPUT_DIRECTORY = "/home/akbis/PycharmProjects/AgenticCodeAnalysis/src/agenticCodeAnalysis/output"
OUTPUT_FILE_NAME = "Code_Analysis_Report.md"
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE_NAME)
ANALYSIS_LANGUAGE = "java"

# --- Initialization ---
print("Initializing Agents and Tasks...")

# 1. Create all possible analysis agents and tasks
agents = create_code_analysis_agents(language=ANALYSIS_LANGUAGE, llm=gemini)
tasks = create_code_analysis_tasks(agents=agents)
agents_list = list(agents.keys())
print(f"Available Agents: {agents_list}")

# 2. Define tools available to the architect
default_tools = [
    get_directory_read_tool(PROJECT_DIRECTORY),
    get_file_read_tool()
]

# 3. Create the Architect Agent and Task
print("Creating Architect Agent...")
architect_agent, architect_task = get_architect(
    llm=gemini,
    agent_list=str(agents_list),  # Pass as string representation
    tools=default_tools,
    project_directory=PROJECT_DIRECTORY
)

# --- Stage 1: Agent Selection (Architect Crew) ---
print("\n--- STAGE 1: Starting Architect Crew (Agent Selection) ---")
architect_crew = Crew(
    agents=[architect_agent],
    tasks=[architect_task],
    process=Process.sequential,
    verbose=True,
    max_rpm=5
)

# Kickoff the architect crew to select the necessary agents
architect_result = architect_crew.kickoff()

# The output of the architect task should be the list of selected agents
# It's crucial that architect_task.output is correctly formatted (e.g., a JSON string or a list of strings)
try:
    # Attempt to parse the output as a JSON list of strings (preferred way)
    selected_agent_names = json.loads(architect_task.output)
    if not isinstance(selected_agent_names, list):
        raise ValueError("Output is not a list.")
except (json.JSONDecodeError, TypeError, ValueError):
    print("WARNING: Architect output is not a valid JSON list. Falling back to simple string conversion.")
    # Fallback: relies on the architect's output being a string that can be easily split/parsed
    try:
        # Evaluate the string output as a Python literal (be careful with eval)
        selected_agent_names = eval(str(architect_task.output))
    except Exception as e:
        print(f"ERROR: Could not parse architect output even with eval. Using empty list. Error: {e}")
        selected_agent_names = []

print(f"\nArchitect's Selected Agents: {selected_agent_names}")

# Prepare the agents and tasks for the second crew
selected_agents = [agents[name] for name in selected_agent_names if name in agents]
selected_tasks = [tasks[name] for name in selected_agent_names if name in tasks]

if not selected_agents:
    print("No valid agents were selected. Exiting analysis.")
    exit()

# 4. Create the Manager Agent and Task
manager_agent, manager_task = create_manager_agent(llm=gemini, language=ANALYSIS_LANGUAGE)
selected_tasks.append(manager_task)  # The manager's task is usually the final task in the sequence

# --- Stage 2: Code Analysis (Analysis Crew) ---
print("\n--- STAGE 2: Starting Analysis Crew (Code Execution) ---")

analysis_crew = Crew(
    agents=selected_agents,
    tasks=selected_tasks,
    process=Process.sequential,
    verbose=True,
    max_rpm=5,
    manager_agent=manager_agent  # This agent guides the whole process
)

# Kickoff the analysis crew
analysis_result = analysis_crew.kickoff()
print("\nAnalysis Complete.")

# --- Output Handling ---
final_output = manager_task.output
print("\n--- Final Manager Output ---")
print(final_output)

# 5. Write the final output to a file
print(f"\nWriting output to: {OUTPUT_FILE_PATH}")

# Ensure the output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# Write the output
with open(OUTPUT_FILE_PATH, "w") as f:  # Use 'w' to overwrite, or 'a' if you want to append to a log
    f.write(str(final_output))

print("Operation finished successfully.")