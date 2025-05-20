import os
from crewai import Crew, Process
from agents import FinanceCrewAgents
from tasks import FinanceCrewTasks

class FinanceCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = FinanceCrewAgents()
        self.tasks = FinanceCrewTasks()

    def run(self):
        researcher = self.agents.market_researcher()
        analyst = self.agents.investment_analyst()
        writer = self.agents.financial_writer()

        research_task = self.tasks.research_task(researcher, self.inputs)
        analysis_task = self.tasks.analysis_task(analyst, [research_task])
        writing_task = self.tasks.writing_task(writer, [analysis_task], self.inputs)

        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        return crew.kickoff()

if __name__ == "__main__":
    print("📈 Welcome to the Investment Recommendation Crew")
    topic = input("What financial topic or market are you interested in? ")
    detailed_questions = input("What specific investment-related questions or concerns do you have? ")

    inputs = f"Topic: {topic}\nDetails: {detailed_questions}"
    finance_crew = FinanceCrew(inputs)
    result = finance_crew.run()

    print("\n\n🔍 Investment Recommendation Report:")
    print(result)
