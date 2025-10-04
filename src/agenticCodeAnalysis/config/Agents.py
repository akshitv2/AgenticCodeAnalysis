from crewai import Agent, LLM
from typing import List, Any

# --- Agent Parameters (For illustrative purposes, these would be passed when defining a Crew) ---
languages: List[str] = ["Python", "JavaScript", "Java", "Go", "Rust", "C++"]
llm_model: str = "gpt-4-turbo"  # Replace with your actual LLM configuration


def create_code_analysis_agents(llm: LLM, language: str) -> dict[str | Any, Agent | tuple[Agent] | Any]:
    """
    Creates a list of specialized CrewAI agents for code and project analysis,
    parameterized to an expertise in a specific programming language.
    """
    base_config = {
        "llm": llm,  # Assumes llm_model is configured
        "verbose": True,
        "allow_delegation": True,
        "backstory": (
            f"A seasoned expert with deep knowledge of {language} and best practices."
        ),
    }

    agents = {"Static Code Analyzer": Agent(
        role=f"{language} Static Code Analyzer",
        goal=(
            f"Identify bugs, stylistic issues, and potential vulnerabilities "
            f"in {language} code without executing it."
        ),
        **base_config,
    ), "Dynamic Code Behavior Analyst": Agent(
        role=f"{language} Dynamic Code Behavior Analyst",
        goal=(
            f"Evaluate the runtime performance, memory usage, and execution flow "
            f"of {language} applications during execution."
        ),
        **base_config,
    ), "Security Auditor": Agent(
        role=f"{language} Security Auditor",
        goal=(
            f"Scan and assess {language} project source code and dependencies "
            f"for common security flaws (e.g., OWASP Top 10, Injection) "
            f"and recommend remediation."
        ),
        **base_config,
    ), "Code Smells Detector": Agent(
        role=f"{language} Code Smells Detector",
        goal=(
            f"Identify and catalog anti-patterns, redundant code, and maintainability "
            f"risks specific to the {language} ecosystem."
        ),
        **base_config,
    ), "Design Pattern Identifier": Agent(
        role=f"{language} Design Pattern Identifier",
        goal=(
            f"Analyze the structure of the {language} project to identify "
            f"implemented design patterns (e.g., MVC, Factory, Observer) "
            f"and evaluate their appropriate usage."
        ),
        **base_config,
    ), "Cyclomatic Complexity Assessor": Agent(
        role=f"{language} Cyclomatic Complexity Assessor",
        goal=(
            f"Calculate and report on the complexity of functions and modules "
            f"in the {language} codebase, pinpointing areas for simplification."
        ),
        **base_config,
    ), "Module Dependency Mapper": Agent(
        role=f"{language} Module Dependency Mapper",
        goal=(
            f"Map out the inter-module and external library dependencies "
            f"for the {language} project to identify tight coupling."
        ),
        **base_config,
    ), "Architectural Reviewer": Agent(
        role=f"{language} Architectural Reviewer",
        goal=(
            f"Provide a high-level review of the overall system architecture "
            f"for the {language} application, ensuring scalability and adherence "
            f"to modern design principles."
        ),
        **base_config,
    ), "Technical Debt Calculator": Agent(
        role=f"{language} Technical Debt Calculator",
        goal=(
            f"Quantify and prioritize technical debt items within the {language} "
            f"codebase based on maintainability, age, and severity."
        ),
        **base_config,
    ), "Refactoring Strategist": Agent(
        role=f"{language} Refactoring Strategist",
        goal=(
            f"Develop a step-by-step strategy for refactoring specific "
            f"high-risk or high-complexity sections of the {language} code."
        ),
        **base_config,
    ), "Effort Estimator (COCOMO Expert)": Agent(
        role=f"{language} Effort Estimator (COCOMO Expert)",
        goal=(
            f"Analyze the size and complexity of the {language} project "
            f"to provide effort and time estimates for future feature "
            f"development or bug fixes."
        ),
        **base_config,
    ), "Library Vulnerability Tracker": Agent(
        role=f"{language} Library Vulnerability Tracker",
        goal=(
            f"Identify all third-party libraries used in the {language} "
            f"project and check for known CVEs (Common Vulnerabilities and Exposures)."
        ),
        **base_config,
    ), "Unit Test Coverage Analyst": Agent(
        role=f"{language} Unit Test Coverage Analyst",
        goal=(
            f"Evaluate the quality and coverage of existing unit and integration "
            f"tests for the {language} codebase."
        ),
        **base_config,
    ), "Performance Bottleneck Finder": Agent(
        role=f"{language} Performance Bottleneck Finder",
        goal=(
            f"Identify specific code segments in {language} that are "
            f"causing execution slowness and propose optimized alternatives."
        ),
        **base_config,
    ), "Documentation Quality Assessor": Agent(
        role=f"{language} Documentation Quality Assessor",
        goal=(
            f"Review and score the quality, completeness, and accuracy "
            f"of in-code and external documentation for the {language} project."
        ),
        **base_config,
    ), "Code Review Specialist": Agent(
        role=f"{language} Code Review Specialist",
        goal=(
            f"Act as a virtual senior developer, providing constructive, "
            f"in-depth code review comments for pull requests in {language}."
        ),
        **base_config,
    ), "Compiler/Interpreter Settings Expert": Agent(
        role=f"{language} Compiler/Interpreter Settings Expert",
        goal=(
            f"Analyze and recommend optimal compiler flags or interpreter settings "
            f"for the {language} project to improve security, performance, or debugging."
        ),
        **base_config,
    ), "API Contract Validator": Agent(
        role=f"{language} API Contract Validator",
        goal=(
            f"Review the public API surface of the {language} application "
            f"to ensure consistency, RESTfulness, and adherence to established contracts."
        ),
        **base_config,
    ), "Environment Configuration Auditor": Agent(
        role=f"{language} Environment Configuration Auditor",
        goal=(
            f"Check project configuration files (e.g., Dockerfiles, package.json, requirements.txt) "
            f"for security issues, best practices, and consistency with the {language} environment."
        ),
        **base_config,
    ), "Code Duplication Finder": Agent(
        role=f"{language} Code Duplication Finder",
        goal=(
            f"Utilize techniques to find and report on duplicated code blocks "
            f"and functions across the {language} codebase."
        ),
        **base_config,
    ), "Error Handling and Logging Expert": Agent(
        role=f"{language} Error Handling and Logging Expert",
        goal=(
            f"Assess the robustness of error handling (try/catch, exceptions) "
            f"and the clarity/completeness of logging mechanisms in the {language} code."
        ),
        **base_config,
    ), "Maintainability Index Scorer": Agent(
        role=f"{language} Maintainability Index Scorer",
        goal=(
            f"Calculate and provide the Maintainability Index score for the {language} "
            f"project, based on complexity, lines of code, and comments."
        ),
        **base_config,
    ), "Build System Analyst": Agent(
        role=f"{language} Build System Analyst",
        goal=(
            f"Examine the build configuration and processes (e.g., package scripts, "
            f"CI/CD setup) for the {language} project for efficiency and correctness."
        ),
        **base_config,
    ), "Legacy Code Modernizer": Agent(
        role=f"{language} Legacy Code Modernizer",
        goal=(
            f"Identify and propose replacements for deprecated language features "
            f"or libraries in the older sections of the {language} codebase."
        ),
        **base_config,
    )}

    return agents
