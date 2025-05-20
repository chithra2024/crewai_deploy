from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

class FinanceCrewAgents:
    def __init__(self):
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape = ScrapeWebsiteTool()

        # Language models
        self.gpt4 = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        self.gemma = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="gemma2-9b-it")

        # Select model
        self.selected_llm = self.gpt4

    def market_researcher(self):
        return Agent(
            role='Market Researcher',
            goal='To investigate financial trends, macroeconomic indicators, and emerging market risks or opportunities.',
            backstory="You are a top-tier financial researcher skilled at using web data and tools to find actionable insights for investors.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3
        )

    def investment_analyst(self):
        return Agent(
            role='Investment Analyst',
            goal='To analyze research insights and produce a strategic investment recommendation with rationale and risk analysis.',
            backstory="You are a data-driven investment expert skilled in portfolio strategies, risk evaluation, and industry sector analysis.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3
        )

    def financial_writer(self):
        return Agent(
            role='Financial Writer',
            goal='To compile a professional investment report with key data, insights, actionable recommendations, and links to resources.',
            backstory="You are a skilled finance writer experienced in summarizing technical content for decision-makers and investors.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3
        )
