from crewai import Task

class FinanceCrewTasks:

    def research_task(self, agent, inputs):
        return Task(
            agent=agent,
            description=f"Research the current financial market scenario based on: {inputs}. Search for macroeconomic data, stock/sector news, policy updates, and global trends. Use https://finance.yahoo.com and trusted sources.",
            expected_output="A comprehensive report on market trends, investment opportunities, and economic outlook."
        )

    def analysis_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description=f"Review this market research report: {context}. Perform risk-reward analysis and suggest optimal investment options (stocks, ETFs, sectors, assets).",
            expected_output="A strategic investment recommendation with rationale, potential returns, and associated risks."
        )

    def writing_task(self, agent, context, inputs):
        return Task(
            agent=agent,
            context=context,
            description=f"Summarize this investment recommendation report: {context}. Include 3 key insights, 3 actionable investment tips, and provide links to 3 recent financial articles, 3 finance books (with authors), and 3 online financial tools useful for investors.",
            expected_output="An executive-style investment report with summaries, links, tools, and actionable advice."
        )
