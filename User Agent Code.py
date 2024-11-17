from langchain.agents import AgentExecutor, initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from typing import Dict, Any

class UserAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.llm = OpenAI(temperature=0)  # LLM for user interaction
        self.tools = []  # Add tools if needed for advanced functionalities

        # Initialize the agent with tools and prompts
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent="zero-shot-react-description",
            verbose=True
        )

    def collect_travel_request(self, query: str) -> Dict[str, Any]:
        """
        Collects travel request details from the user via LLM interaction.
        """
        prompt = PromptTemplate(
            input_variables=["query"],
            template="You are a personal travel assistant. Respond to this travel request: {query}"
        )
        response = self.agent.run(prompt.format(query=query))
        # Parse and return data as structured information
        return {"user_id": self.user_id, "request": query, "response": response}

    def send_to_orchestrator(self, travel_data: Dict[str, Any], orchestrator):
        """
        Sends travel request to the orchestrator.
        """
        orchestrator.receive_data(travel_data)
