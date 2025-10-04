from crewai import Agent, Task

def create_manager_agent(language: str, llm) -> tuple[Agent, Task]:
    """
    Creates a specialized Manager Agent responsible for oversight, synthesis,
    and final report generation.
    """
    manager_agent = Agent(
        role=f"Chief Software Quality Manager ({language} Expert)",
        goal=(
            f"Supervise the entire code analysis crew, synthesize all findings "
            f"from the specialized {language} agents, and compile a single, "
            f"comprehensive, high-level Code Audit Report in Markdown format."
        ),
        backstory=(
            f"A veteran leader and technical program manager with a deep understanding of {language} "
            f"development lifecycle and best practices. This agent's primary focus is not "
            f"individual analysis but **executive-level synthesis, prioritization, and communication** "
            f"of the crew's findings to stakeholders. Ensures the final report is actionable, clear, "
            f"and professionally formatted."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,  # Managers typically don't delegate their final reporting task
    )
    """
        Creates the final task that uses the Manager Agent to compile the report.
        This task should be the final one in your Crew's execution plan.
        """
    final_task = Task(
        description=(
            "**FINAL REPORT GENERATION**: Take the results from ALL previous specialized analysis tasks "
            "(Static Analysis, Security Audit, Complexity, Debt, Performance, etc.). "
            "Synthesize these findings into a single, cohesive, professional 'Code Audit Report' "
            "in high-quality Markdown format. The report MUST include a 'Executive Summary', "
            "'Priority Action Items' (ranked by severity/cost), and detailed sections "
            "for each area of analysis. Ensure all data is cross-referenced and the tone is professional."
        ),
        agent=manager_agent,
        expected_output="A full, professional Code Audit Report in Markdown format (MD).",
        output_file="Code_Analysis_Report.md"  # The requested final output file
    )

    return manager_agent, final_task