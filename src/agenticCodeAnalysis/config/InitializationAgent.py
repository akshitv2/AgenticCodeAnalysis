from crewai import Agent, Task
from crewai_tools import DirectoryReadTool, FileReadTool


# Assuming the repository is available locally, you might need a tool to read the files.
# For simplicity, we'll define a generic Tool that could represent any method
# of accessing the repo (e.g., a custom 'GitCloneTool' or 'CodebaseExplorerTool').
# We'll use the existing DirectoryReadTool for reading the code structure.
def get_architect(llm=None, agent_list=None, tools=None, project_directory=""):
    if tools is None:
        tools = []
    if agent_list is None:
        agent_list = []
    analysis_architect = Agent(
        role='Code Analysis Architect',
        goal=f"Determine the right agents needed to analyse this project. Currently available agents are: {agent_list}",
        backstory=(
            "You are an expert in multi-agent system design and software architecture. "
            "You are required to choose a team of experts best suited from this job."
        ),
        tools=tools,  # Tools to read the repository files
        verbose=True,
        llm=llm
    )
    architect_task = Task(
        description=(
            f"Review the submitted repository located at {project_directory} and return list of agents required for analysis from following list: {agent_list}"
        ),
        expected_output=(
            "A python list of the minimum required agents from the ones provided. "
        ),
        agent=analysis_architect,
    )
    return analysis_architect, architect_task
