import os

from crewai_tools.tools.scrape_website_tool.scrape_website_tool import ScrapeWebsiteTool
from crewai_tools.tools.serper_dev_tool.serper_dev_tool import SerperDevTool
from dotenv import load_dotenv
from crewai import Crew, Task, Process, Agent
from crewai_tools import DirectoryReadTool
import os
from src.agenticCodeAnalysis.Loaders.AgentLoader import read_yaml_config, get_agents, get_tasks
from src.agenticCodeAnalysis.llms.gemini import gemini
from src.agenticCodeAnalysis.llms.local import local_llm

java_project_directory = '/media/akbis/drive/dev/Agentic-Experiments/temp/spring-boot-ecommerce'
tools = {
    'directory_read_tool': DirectoryReadTool(directory=java_project_directory),
    'search_tool': SerperDevTool(),
    'fetch_webpage_tool': ScrapeWebsiteTool()
}
agents_file = "config/agents.yaml"
agents = get_agents(agents_file, tools = tools, llm=gemini)
tasks_file = "config/tasks.yaml"
tasks = get_tasks(tasks_file, agents = agents)

agents_array = [agents[i] for i in agents.keys()]
tasks_array = [tasks[i] for i in tasks.keys()]
# specialist_agents = [agents[i] for i in ['journey_developer', 'java_developer', 'api_developer']]
# lead_agent = agents['lead_agent']
# specialist_tasks  = [tasks[i] for i in ['journey_task', 'application_task', 'api_task']]
# lead_task = tasks['analysis_task']

documentation_crew = Crew(
    agents=agents_array,
    tasks=tasks_array,
    process=Process.sequential,
    verbose=True,
    manager_agent=agents["lead_agent"]
)
documentation_crew.kickoff()

print("###############################################")
print("################# RESULT ######################")
print("###############################################")

with open("output.md","a") as f:
    for i in tasks_array:
        print(i.output)
        f.write(str(i.agent.role) + "\n")
        f.write("\n  ")
        f.write(str(i.output))

