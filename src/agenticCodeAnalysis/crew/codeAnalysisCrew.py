from crewai import Crew, Task, Process, Agent
import os

from src.agenticCodeAnalysis.config.Agents import *
from src.agenticCodeAnalysis.config.Tasks import *
from src.agenticCodeAnalysis.llms.gemini import gemini
from src.agenticCodeAnalysis.llms.local import local_llm

def get_code_analysis_crew():

    selected_llm = gemini
    # project_directory = '/mnt/85e3eeea-3bda-4255-95a1-833fffd20e34/dev/Agentic-Experiments/temp/spring-boot-ecommerce'
    project_directory = '/home/akbis/PycharmProjects/AgenticCodeAnalysis/src/agenticCodeAnalysis'

    output_directory = "/home/akbis/PycharmProjects/AgenticCodeAnalysis/src/agenticCodeAnalysis/output"
    output_file_name = "output.md"
    language = "python"

    default_tools = [get_directory_read_tool(project_directory), get_file_read_tool()]
    security_analyst_tools = [
        get_directory_read_tool(project_directory),
        get_file_read_tool(),
        get_search_tool(),
        get_fetch_webpage_tool()
    ]

    documentation_agent_tools = [
        get_search_tool(),
        get_fetch_webpage_tool(),
        get_file_write_tool(output_directory, output_file_name)
    ]


    lead_agent = get_lead_agent(project_directory=project_directory, language=language, llm=selected_llm, tools=default_tools)
    journey_dev = get_journey_developer(project_directory=project_directory, language=language, llm=selected_llm,
                                        tools=default_tools)
    app_dev = get_application_developer(project_directory=project_directory, language=language, llm=selected_llm,
                                        tools=default_tools)
    api_dev = get_api_developer(project_directory=project_directory, language=language, llm=selected_llm, tools=default_tools)
    security_analyst = get_security_analyst(project_directory=project_directory, language=language, llm=selected_llm,
                                            tools=security_analyst_tools)
    documentation_agent = get_documentation_agent(llm=selected_llm, tools= documentation_agent_tools)
    agents_array = [lead_agent, journey_dev, app_dev, api_dev, security_analyst, documentation_agent]

    lead_task = get_analysis_task(language, lead_agent)
    journey_task = get_journey_task(language, journey_dev)
    application_task = get_application_task(language, app_dev)
    api_task = get_api_task(language, api_dev)
    security_task = get_security_analysis_task(language, security_analyst)
    documentation_task = get_documentation_task(documentation_agent)
    tasks_array = [lead_task, journey_task, application_task, api_task, security_task, documentation_task]

    documentation_crew = Crew(
        agents=agents_array,
        tasks=tasks_array,
        process=Process.sequential,
        verbose=True,
        manager_agent=lead_agent,
        max_rpm=5
    )

    return documentation_crew,agents_array, tasks_array
# documentation_crew.kickoff()
#
# print("###############################################")
# print("################# RESULT ######################")
# print("###############################################")
#
# print(documentation_task.output)
#
# output_file = "../output.md"
# if os.path.exists(output_file):
#     os.remove(output_file)
#
# with open(output_file, "a") as f:
#     f.write(str(documentation_task.output))
