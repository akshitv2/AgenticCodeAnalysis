from src.agenticCodeAnalysis.config.Tools import *
from crewai import Agent
from typing import List

def get_lead_agent(project_directory: str = ".", language: str = "Java", llm = None, tools=None) -> Agent:
    """
    Creates the Development Lead agent, parameterized by language.
    """
    if tools is None:
        tools = []

    return Agent(
        role=f"Development Lead ({language} Specialist)",
        goal="Analyze the provided project code, distributing tasks and classes to each developer.",
        backstory=f"A senior expert in {language} coding and management.",
        tools=[get_directory_read_tool(project_directory)],
        llm = llm
    )

def get_journey_developer(project_directory: str = ".", language: str = "Java", llm = None, tools=[]) -> Agent:
    """
    Creates the Senior Journey Developer agent, parameterized by language.
    Goal: Identify flow of control and document the purpose of each class/module.
    """
    return Agent(
        role=f"Senior Journey Developer ({language})",
        goal="Analyze the provided project code, identifying flow of control and finally document what is the purpose of each class/module and what is the overall functionality.",
        backstory=f"A meticulous expert in {language} development and architecture, specializing in code analysis and journeys.",
        tools=tools,
        llm = llm
    )

def get_application_developer(project_directory: str = ".", language: str = "Java", llm = None, tools=[]) -> Agent:
    """
    Creates the Senior application developer agent, parameterized by language.
    Goal: Identify and document methods/functions exposed by each class/module.
    """
    return Agent(
        role=f"Senior {language} application developer",
        goal=f"Analyze the provided {language} project code, identify and document methods/functions exposed by each class/module.",
        backstory=f"A meticulous expert in {language} development and architecture, specializing in code analysis and application development.",
        tools=tools,
        llm = llm
    )

def get_api_developer(project_directory: str = ".", language: str = "Java", llm = None, tools=[]) -> Agent:
    """
    Creates the Senior API developer agent, parameterized by language.
    Goal: Find and document the controller APIs exposed.
    """
    return Agent(
        role=f"Senior {language} api developer",
        goal=f"Analyze the provided {language} project code, find and document the controller apis exposed.",
        backstory=f"A meticulous expert in {language} development and architecture, specializing in apis and integration.",
        tools=tools,
        llm = llm
    )

def get_security_analyst(project_directory: str = ".", language: str = "Java", llm = None, tools=[]) -> Agent:
    """
    Creates the Senior Cybersecurity Specialist agent, parameterized by language.
    Goal: Find dependencies/libraries and check online for vulnerabilities.
    """

    return Agent(
        role="Senior Cybersecurity Specialist",
        goal=f"Analyze the provided {language} project code, find any files that contain dependencies and libraries and check online if they have any vulnerabilities",
        backstory="A meticulous expert in security analysis specializing in application security.",
        tools=tools,
        llm = llm
    )


def get_documentation_agent(llm = None, tools=None) -> Agent:

    if tools is None:
        tools = []
    return Agent(
        role="Documentation Specialist",
        goal=f"Combine the reports of all of the specialists.",
        backstory="A meticulous expert excelling at making comprehensive reports",
        tools=tools,
        llm = llm
    )