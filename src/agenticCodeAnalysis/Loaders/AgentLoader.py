import yaml
from crewai import Agent, Task


def read_yaml_config(filepath):
    """Reads a YAML configuration file and returns the data as a Python dictionary."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None

def get_agents(filepath, tools=None, llm = None)->dict:
    if tools is None:
        tools = dict()
    agent_data = read_yaml_config(filepath)
    agents = {}
    for agent_id in agent_data["agents"]:
        agent = agent_data["agents"][agent_id]
        if agent["tools"]:
            for i in range(0,len(agent["tools"])):
                agent["tools"][i] = tools[agent["tools"][i]]
        if llm is not None:
            agent["llm"] = llm
        agents[agent_id]=Agent(**agent)
    return agents

def get_tasks(filepath, agents=None)->dict:
    if agents is None:
        agents = dict()
    task_data = read_yaml_config(filepath)
    tasks = {}
    for task_id in task_data["tasks"]:
        task = task_data["tasks"][task_id]
        task["agent"] = agents[task["agent"]]
        tasks[task_id]=Task(**task)
    return tasks
