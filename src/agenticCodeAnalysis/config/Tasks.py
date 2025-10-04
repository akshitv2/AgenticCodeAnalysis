from crewai import Task
from typing import List, Any
# Assuming you have the agents created by calling create_code_analysis_agents(language)
# You will need to import the function and call it in your main crew script.

# --- Task Parameters ---
project_context_placeholder: str = (
    "Analyze the provided source code, focusing on the latest changes or the 'src' directory."
    "The analysis should be comprehensive and actionable."
)


def create_code_analysis_tasks(agents: dict[str | Any, Any]) -> dict[str | Any, Task | Any]:
    tasks = {
        "Static Code Analyzer": Task(
            description=(
                f"Perform a static analysis of the project's source code. "
                f"Identify and list all critical bugs, stylistic inconsistencies (linting errors), "
                f"and potential memory or resource leaks. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Static Code Analyzer"],
            expected_output="A detailed list of static analysis findings, categorized by severity (Critical, Major, Minor).",
        ),
        "Dynamic Code Behavior Analyst": Task(
            description=(
                f"Simulate or analyze runtime logs to evaluate dynamic code behavior. "
                f"Report on execution flow anomalies, excessive memory consumption, "
                f"and resource utilization under load conditions. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Dynamic Code Behavior Analyst"],
            expected_output="A report on runtime performance bottlenecks and memory usage statistics.",
        ),
        "Security Auditor": Task(
            description=(
                f"Conduct a comprehensive security audit on the codebase and its configuration. "
                f"Focus on common web and application security flaws (e.g., SQL Injection, XSS, insecure dependencies). "
                f"Identify any hardcoded secrets or sensitive credentials. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Security Auditor"],
            expected_output="A list of security vulnerabilities found, ranked by CVSS score or severity, with clear remediation steps.",
        ),
        "Code Smells Detector": Task(
            description=(
                f"Detect and catalog all 'code smells,' anti-patterns, and signs of low maintainability. "
                f"This includes overly complex methods, duplicate logic, and dead code. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Code Smells Detector"],
            expected_output="A prioritized list of code smells, indicating the file and line number for each issue.",
        ),
        "Design Pattern Identifier": Task(
            description=(
                f"Analyze the structural organization of the project to identify implemented architectural and design patterns (e.g., MVC, Singleton, Strategy). "
                f"Critique whether these patterns are used correctly and appropriately. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Design Pattern Identifier"],
            expected_output="A summary of identified design patterns and an evaluation of their correct application within the project.",
        ),
        "Cyclomatic Complexity Assessor": Task(
            description=(
                f"Calculate the Cyclomatic Complexity for the top 10 largest and most critical functions/modules. "
                f"Highlight any function with a complexity score above 10, as these are primary refactoring targets. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Cyclomatic Complexity Assessor"],
            expected_output="A table listing functions, their calculated complexity scores, and a recommendation for simplification.",
        ),
        "Module Dependency Mapper":Task(
            description=(
                f"Map all internal and external dependencies (libraries, modules, services) used by the project. "
                f"Identify any instance of tight coupling that violates modular design principles. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Module Dependency Mapper"],
            expected_output="A dependency graph analysis, highlighting circular or overly complex relationships.",
        ),
        "Architectural Reviewer":Task(
            description=(
                f"Review the project's macro-level architecture (e.g., microservices, monolithic, tiered). "
                f"Assess its scalability, deployment strategy, and adherence to modern architectural standards. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Architectural Reviewer"],  # Accessing the agent from the tuple
            expected_output="A high-level architectural review, including strengths, weaknesses, and key recommendations for modernization.",
        ),
        "Technical Debt Calculator": Task(
            description=(
                f"Quantify and prioritize the total technical debt. "
                f"Use a simplified model (e.g., cost-of-fix vs. impact) to categorize debt items (e.g., 'Must Fix Now', 'Address Next Quarter'). "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Technical Debt Calculator"],
            expected_output="A prioritized list of technical debt items with estimated effort (time/cost) to resolve each.",
        ),
        "Refactoring Strategist":Task(
            description=(
                f"Based on input from the Technical Debt Calculator and Complexity Assessor, "
                f"formulate a concrete, step-by-step refactoring plan for one major high-risk module. "
                f"The plan must minimize disruption. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Refactoring Strategist"],
            expected_output="A phased refactoring plan (e.g., 5 steps) for a specific module, including intermediate testing points.",
        ),
        "Effort Estimator (COCOMO Expert)":Task(
            description=(
                f"Using COCOMO or a similar model, estimate the effort (person-months) required to implement a single, significant new feature (e.g., a new user dashboard) "
                f"given the current project size and complexity. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Effort Estimator (COCOMO Expert)"],
            expected_output="A clear effort estimate (e.g., 3 person-months) and the calculation inputs used (e.g., LOC, complexity multipliers).",
        ),
        "Library Vulnerability Tracker":Task(
            description=(
                f"List all third-party libraries and check them against public databases for known Common Vulnerabilities and Exposures (CVEs). "
                f"Highlight any library that is both vulnerable and critical to the project. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Library Vulnerability Tracker"],
            expected_output="A list of vulnerable dependencies, their associated CVEs, and recommended version upgrades.",
        ),
        "Unit Test Coverage Analyst":Task(
            description=(
                f"Analyze the existing unit and integration tests. Report on the calculated test coverage percentage (if available) and critique the quality of the tests. "
                f"Identify areas of business logic with inadequate testing. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Unit Test Coverage Analyst"],
            expected_output="A report on test coverage and quality, identifying specific files or features that require new or improved tests.",
        ),
        "Performance Bottleneck Finder":Task(
            description=(
                f"Identify and report on the top 3 performance-degrading code segments. "
                f"Provide an optimized code snippet as an alternative for each bottleneck. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Performance Bottleneck Finder"],
            expected_output="A list of the top 3 bottlenecks with detailed explanation and optimized code samples.",
        ),
        "Documentation Quality Assessor":Task(
            description=(
                f"Score the quality of both in-code comments/docstrings and external documentation (e.g., README, API docs). "
                f"Identify gaps where documentation is missing or inaccurate. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Documentation Quality Assessor"],
            expected_output="A score (e.g., 8/10) for documentation quality, listing specific areas needing improvement.",
        ),
        "Code Review Specialist":Task(
            description=(
                f"Act as a final senior reviewer for a major pull request (or the entire project). "
                f"Provide a summary of the code's readiness for production, focusing on maintainability and clarity. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Code Review Specialist"],
            expected_output="A concise, high-level production readiness review and final sign-off recommendation.",
        ),
        "Compiler/Interpreter Settings Expert":Task(
            description=(
                f"Review the project's build settings (e.g., compiler flags, environment variables, dependencies) "
                f"and recommend changes to improve performance, security, or debugging capabilities. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Compiler/Interpreter Settings Expert"],
            expected_output="A list of recommended compiler/interpreter configuration changes and the rationale for each.",
        ),
        "API Contract Validator":Task(
            description=(
                f"Review all public-facing API endpoints or method signatures. "
                f"Check for consistency in naming, data types, error codes, and adherence to REST/language-specific contract standards. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["API Contract Validator"],
            expected_output="A report detailing any API contract inconsistencies or violations.",
        ),
        "Environment Configuration Auditor":Task(
            description=(
                f"Audit configuration files (Docker, package manager files, environment scripts) for security issues "
                f"(e.g., unnecessary privileges, unpinned versions) and best practice compliance. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Environment Configuration Auditor"],
            expected_output="A checklist of configuration issues and recommended best practices for the project environment.",
        ),
        "Code Duplication Finder":Task(
            description=(
                f"Apply code duplication detection algorithms (e.g., token-based, AST-based) across the entire codebase. "
                f"Report the largest and most frequent duplicated code blocks. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Code Duplication Finder"],
            expected_output="A summary of code duplication instances, including the files and lines involved.",
        ),
        "Error Handling and Logging Expert":Task(
            description=(
                f"Analyze how exceptions and errors are handled (try/catch blocks, exception hierarchy). "
                f"Critique the logging strategy: is it too verbose, not detailed enough, or inconsistent? "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Error Handling and Logging Expert"],
            expected_output="A review of error handling robustness and a list of logging improvements.",
        ),
        "Maintainability Index Scorer":Task(
            description=(
                f"Calculate the final Maintainability Index (MI) score for the entire project. "
                f"This requires integrating data from complexity, LOC, and comment density metrics. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Maintainability Index Scorer"],
            expected_output="The final calculated Maintainability Index score (e.g., 75/100) and its interpretation.",
        ),
        "Build System Analyst":Task(
            description=(
                f"Examine the CI/CD pipeline, package scripts, and overall build process. "
                f"Identify areas for performance improvement in build times, artifact size, or dependency resolution. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Build System Analyst"],
            expected_output="A review of the build system, highlighting inefficiencies and potential speedups.",
        ),
        "Legacy Code Modernizer":Task(
            description=(
                f"Identify deprecated language features, old library versions, or outdated coding styles in legacy files. "
                f"Provide concrete suggestions on how to update them to modern standards. "
                f"Context: {project_context_placeholder}"
            ),
            agent=agents["Legacy Code Modernizer"],
            expected_output="A list of legacy code modernization targets with suggested modern alternatives.",
        )
    }

    return tasks