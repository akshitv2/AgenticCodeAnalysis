# Agentic AI Code Audit and Analysis Engine

## Project Overview

Built on the `crewai` platform, it harnesses the power of AI to empower them into agents with access to tools. It
features a team of smart, specialized agents that dig deep into your codebase, working together like a virtual
consulting firm to spot issues and suggest fixes.

The problem-solving is done in two major steps:

- **Smart Team Selection**: A Code Analysis Architect agent scans your project’s structure and picks the right mix of
  expert agents (from a pool of 24) for the job. This keeps things efficient and focused.
- **Detailed Analysis & Reporting**: The chosen agents tackle their tasks, and a Chief Software Quality Manager pulls
  their findings into a clear, actionable report.

It’s like having a dedicated team of code experts on your side.

## Key Features

| **Feature**                 | **What It Does**                                                                                                                   | **Who’s Involved**                             |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| **Smart Task Assignment**   | The Architect reads your project’s layout to pick only the tasks that matter, saving time and resources.                           | Code Analysis Architect                        |
| **Specialized Experts**     | 24 AI agents cover everything from code basics to big-picture architecture.                                                        | Security Auditor, Refactoring Strategist, etc. |
| **Works with Any Language** | Agents adapt to your codebase’s language (Python, Java, C++, etc.) and can use any LLM, like OpenApi, Gemini or a local model.     | All 24 Agents                                  |
| **Clear Reports**           | The Chief Software Quality Manager turns technical findings into a polished Markdown report with an executive summary.             | Chief Software Quality Manager                 |
| **Codebase Exploration**    | Agents use `crewai_tools` like `DirectoryReadTool` and `FileReadTool` to navigate and understand your project before analyzing it. | Architect Agent, All Specialist Agents         |

## Getting Started

### What You Need

- Python 3.10 or higher
- An LLM API key (e.g., Google’s Gemini or a local LLM setup)

### Setup Steps

1. **Clone the Repo**:
   ```bash
   git clone <your_repo_url>
   cd AgenticCodeAnalysis
   ```

2. **Install Dependencies**:
   You’ll need `crewai`, `crewai-tools`, and your LLM’s SDK.
   ```bash
   pip install crewai crewai-tools pydantic google-genai
   ```

3. **Set Up Environment**:
   Add your LLM API key to your environment variables.
   ```bash
   # Example for Gemini:
   export GEMINI_API_KEY="YOUR_API_KEY_HERE"
   ```

## How to Use It

### Step 1: Configure (`main.py`)

Edit `main.py` to point to your project and set key details:

| **Setting**         | **What It Means**                                     | **Example**                          |
|---------------------|-------------------------------------------------------|--------------------------------------|
| `project_directory` | Path to the codebase you want to analyze.             | `/path/to/my/microservice-repo`      |
| `language`          | Your codebase’s main programming language.            | `java` (or Python, JavaScript, etc.) |
| `llm`               | The LLM you’re using (e.g., Gemini or a local model). | `gemini`                             |

### Step 2: Run the Analysis

Kick things off from your terminal:

```bash
python main.py
```

You’ll see updates as the Architect picks the team and the Analysis Crew does its work.

### Step 3: Check the Report

When it’s done, you’ll get a polished report:

- `Code_Analysis_Report.md`

This file sums up the findings, highlights key issues, and offers practical next steps.

## Inside the Two-Crew System

### Crew 1: Architect Crew (Team Selection)

A single agent handles the planning.

| **Agent**               | **File**                 | **Job**                                                                                                                 |
|-------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Code Analysis Architect | `InitializationAgent.py` | Checks your project’s setup (e.g., Dockerfile, CI config, dependencies) and picks the right agents from the pool of 24. |

### Crew 2: Analysis Crew (Execution & Reporting)

This crew includes the selected agents plus a manager to wrap things up.

| **Agent**         | **File**                 | **Job**                                                                                                          |
|-------------------|--------------------------|------------------------------------------------------------------------------------------------------------------|
| Specialist Agents | `Agents.py` / `Tasks.py` | Tackle specific tasks like finding security flaws or measuring code complexity. Their results go to the Manager. |
| Manager Agent     | `Manager.py`             | Combines all findings into a clear, high-level report for stakeholders.                                          |

## Analysis Capabilities (The Agent Pool)

The framework has 24 tasks to cover every angle of your codebase. The Architect picks what’s needed:

| CrewAI Expert (Agent Name)           | Primary Responsibility (Focus Area)                                                                                              | Key Expected Output                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Static Code Analyzer                 | Perform static analysis: Identify critical bugs, linting errors, and resource leaks.                                             | Detailed list of static analysis findings, categorized by severity.                                    |
| Dynamic Code Behavior Analyst        | Evaluate dynamic behavior: Simulate/analyze runtime logs for execution anomalies, memory use, and resource utilization.          | Report on runtime performance bottlenecks and memory usage statistics.                                 |
| Security Auditor                     | Conduct a comprehensive security audit: Focus on security flaws (SQL Injection, XSS) and identify hardcoded secrets.             | List of security vulnerabilities, ranked by CVSS/severity, with remediation steps.                     |
| Code Smells Detector                 | Detect and catalog 'code smells,' anti-patterns, and signs of low maintainability (e.g., duplicate logic, complex methods).      | Prioritized list of code smells, indicating the file and line number.                                  |
| Design Pattern Identifier            | Analyze structural organization: Identify and critique the correct application of architectural and design patterns.             | Summary of identified design patterns and an evaluation of their correct application.                  |
| Cyclomatic Complexity Assessor       | Calculate Cyclomatic Complexity: Focus on the top 10 largest/most critical functions.                                            | Table listing functions, their calculated complexity scores, and simplification recommendations.       |
| Module Dependency Mapper             | Map all internal and external dependencies: Identify instances of tight coupling and modular design violations.                  | Dependency graph analysis, highlighting circular or overly complex relationships.                      |
| Architectural Reviewer               | Review macro-level architecture: Assess scalability, deployment strategy, and adherence to modern standards.                     | High-level architectural review with strengths, weaknesses, and modernization recommendations.         |
| Technical Debt Calculator            | Quantify and prioritize technical debt: Categorize debt items using a simplified model (cost-of-fix vs. impact).                 | Prioritized list of technical debt items with estimated effort (time/cost) to resolve each.            |
| Refactoring Strategist               | Formulate a concrete, step-by-step refactoring plan for one major high-risk module.                                              | A phased refactoring plan for a specific module, including intermediate testing points.                |
| Effort Estimator (COCOMO Expert)     | Estimate the effort (person-months) required to implement a single significant new feature using COCOMO or a similar model.      | A clear effort estimate and the calculation inputs used (e.g., LOC, complexity multipliers).           |
| Library Vulnerability Tracker        | Check third-party libraries against public databases for known CVEs.                                                             | List of vulnerable dependencies, their associated CVEs, and recommended version upgrades.              |
| Unit Test Coverage Analyst           | Analyze unit and integration tests: Report coverage percentage and critique test quality, identifying inadequately tested areas. | Report on test coverage and quality, identifying specific features that require new or improved tests. |
| Performance Bottleneck Finder        | Identify and report on the top 3 performance-degrading code segments.                                                            | A list of the top 3 bottlenecks with detailed explanations and optimized code samples.                 |
| Documentation Quality Assessor       | Score the quality of in-code comments/docstrings and external documentation, identifying gaps.                                   | A score for documentation quality, listing specific areas needing improvement.                         |
| Code Review Specialist               | Act as a final senior reviewer: Provide a summary of the code's readiness for production.                                        | Concise, high-level production readiness review and final sign-off recommendation.                     |
| Compiler/Interpreter Settings Expert | Review build settings (compiler flags, environment variables) and recommend changes to improve performance or security.          | List of recommended configuration changes and the rationale for each.                                  |
| API Contract Validator               | Review public-facing API endpoints/signatures: Check for consistency in naming, data types, and adherence to contract standards. | Report detailing any API contract inconsistencies or violations.                                       |
| Environment Configuration Auditor    | Audit configuration files (Docker, package manager files) for security issues and best practice compliance.                      | Checklist of configuration issues and recommended best practices for the project environment.          |
| Code Duplication Finder              | Apply code duplication detection algorithms across the codebase.                                                                 | Summary of code duplication instances, including the files and lines involved.                         |
| Error Handling and Logging Expert    | Analyze exception handling and critique the logging strategy for robustness and consistency.                                     | Review of error handling robustness and a list of logging improvements.                                |
| Maintainability Index Scorer         | Calculate the final Maintainability Index (MI) score for the entire project.                                                     | The final calculated Maintainability Index score and its interpretation.                               |
| Build System Analyst                 | Examine the CI/CD pipeline and overall build process: Identify areas for performance improvement in build times.                 | Review of the build system, highlighting inefficiencies and potential speedups.                        |
| Legacy Code Modernizer               | Identify deprecated language features or outdated coding styles in legacy files.                                                 | List of legacy code modernization targets with suggested modern alternatives.                          |

## Project File Structure

The project is organized for clarity and modularity:

```
.
├── main.py                             # Main script: Sets up LLMs, agents, tasks, and starts both crews.
├── src/
│   └── agenticCodeAnalysis/
│       ├── config/
│       │   ├── Agents.py              # Defines the 24 specialized agents.
│       │   ├── Tasks.py               # Defines the 24 analysis tasks and their outputs.
│       │   ├── Tools.py               # Defines the file and search access tools needed
│       │   ├── InitializationAgent.py  # Defines the Architect agent for team selection.
│       │   └── Manager.py              # Defines the Manager agent for report generation.
│       └── llms/
│           ├── gemini.py               # Config for Google Gemini integration.
│           └── local.py                # Config for local LLM setup (e.g., Ollama).
└── Code_Analysis_Report.md             # The final audit report.
```

## Contributing

Want to help make this better? Any contributions to add new agents, improve the Architect’s selection logic, or
enhance the Manager’s reporting are welcome.
Please fork and raise PR