from src.agenticCodeAnalysis.crew.codeAnalysisCrew import get_code_analysis_crew

if __name__ == '__main__':
    crew = get_code_analysis_crew()
    crew[0].kickoff()