from crewai import Task
from typing import List

def get_analysis_task(language: str = "Java", agent = None) -> Task:
    """
    Creates the analysis task for the Lead Agent.
    Goal: Distribute classes/modules among specialists based on analysis.
    """
    description = f"""
      Using the provided DirectoryReadTool, read and analyze all the {language} source files located in the project directory. 
      Focus on understand which specialist is best suited to handle each process and assign them which classes/modules to read.
      Specialists available are: journey_developer, application_developer, api_developer, security_analyst
    """
    return Task(
        description=description,
        # The agent should be set when forming the crew (e.g., agent=get_lead_agent(language=language))
        agent=agent, # Placeholder. Agent is assigned in the Crew definition.
        expected_output=f"A summary report of the {language} project after assigning each developer their task. (Keep it less than 5 lines and in .md syntax)"
    )

def get_journey_task(language: str = "Java", agent = None) -> Task:
    """
    Creates the journey task for the Journey Developer.
    Goal: Explain the entire flow of control and overall purpose.
    """
    description = f"""
      Using the provided DirectoryReadTool, read and analyze all the {language} files assigned to you. 
      Focus on understand the classes/modules and provide an explanation of the entire journey/flow of control and what it does.
    """
    return Task(
        description=description,
        # The agent should be set when forming the crew (e.g., agent=get_journey_developer(language=language))
        agent=agent, # Placeholder. Agent is assigned in the Crew definition.
        expected_output="A report of flow of control and use of journey. (Do it in 5 lines and in .md syntax)"
    )

def get_application_task(language: str = "Java", agent = None) -> Task:
    """
    Creates the application task for the Application Developer.
    Goal: Document methods/functions exposed and their parameters.
    """
    description = f"""
      Using the provided DirectoryReadTool, read and analyze all the {language} files assigned to you. 
      Focus on understand methods/functions exposed and parameters expected in each.
    """
    return Task(
        description=description,
        # The agent should be set when forming the crew (e.g., agent=get_application_developer(language=language))
        agent=agent, # Placeholder. Agent is assigned in the Crew definition.
        expected_output="A detailed report of methods/functions and parameters across each class/module. (Do it in 20 lines or less and in .md syntax)"
    )

def get_api_task(language: str = "Java", agent = None) -> Task:
    """
    Creates the API task for the API Developer.
    Goal: Report on exposed API endpoints.
    """
    description = f"""
      Using the provided DirectoryReadTool, read and analyze all the {language} files assigned to you. 
      Focus on reporting which apis are exposed in the controllers/handlers.
    """
    return Task(
        description=description,
        # The agent should be set when forming the crew (e.g., agent=get_api_developer(language=language))
        agent=agent, # Placeholder. Agent is assigned in the Crew definition.
        expected_output="Detailed report of api endpoints and how to call them. (Do it in 10 lines or less and in .md syntax)"
    )

def get_security_analysis_task(language: str = "Java", agent = None) -> Task:
    """
    Creates the security analysis task for the Security Analyst.
    Goal: Find and report vulnerabilities in dependencies.
    """
    description = """
      Using the provided DirectoryReadTool, read and analyze all dependency containing files searching for libraries.
      Use search_tool to check their version online and fetch_webpage_tool to fetch pages with info of them. 
      Make a list of all dependencies which have vulnerabilities.
    """
    return Task(
        description=description,
        # The agent should be set when forming the crew (e.g., agent=get_security_analyst(language=language))
        agent=agent, # Placeholder. Agent is assigned in the Crew definition.
        expected_output="Tabular report of libraries and any vulnerabilities in them. Only mention dependency and CVE. (return table in .md syntax)"
    )

def get_documentation_task(agent=None)->Task:
    description = """
         Collect all the outputs from other agents namely analysis, journey developer, application developer, api developer and security analyst.
         Combine all their reports in one big cohesive report which shows each agents report (with proper formatting) in the form of a readme.md file.
       """
    return Task(
        description=description,
        agent=agent,  # Placeholder. Agent is assigned in the Crew definition.
        expected_output="Combined report of all agents with proper separation and proper formatting in form of a md file"
    )