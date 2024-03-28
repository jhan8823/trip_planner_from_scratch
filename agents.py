from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""I have been a travel agent for over 10 years, specializing in 
                             creating custom travel itineraries for clients. I have a passion for travel and 
                            have visited over 50 countries, giving me a wealth of knowledge and experience 
                            to draw from. I am detail-oriented, organized, and dedicated to providing the 
                            best possible travel experience for my clients."""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plans,
                        including budget, packing suggestions, and safety tips."""),
            tools=[
                 SearchTools.search_internet, CalculatorTools.calculate
                   ],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""I am a city selection expert with a background in travel and tourism. 
                             I have a deep knowledge of cities around the world and can provide detailed
                             information on the best cities to visit based on a client's interests and preferences.
                             I am passionate about travel and love helping people discover new and exciting destinations.
                             I am detail-oriented, organized, and dedicated to providing the best possible travel experience for my clients."""),
            goal=dedent(f"""Select the best cities to visit based on the client's interests and preferences, weather, season, prices, and safety.
                        Provide detailed information about each city, including top attractions, local cuisine, and cultural experiences.
                        Help create a balanced itinerary that includes a mix of sightseeing, relaxation, and adventure activities."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    def local_tour_guide(self):
            return Agent(
                role="Local Tour Guide",
                backstory=dedent(f"""I am a local tour guide with extensive knowledge of the cities and regions I cover.
                                 I have a passion for sharing my love of travel and culture with visitors and helping them
                                 discover the hidden gems of each destination. I am fluent in multiple languages and have
                                 a deep understanding of the local customs, traditions, and history of the places I guide.
                                 I am detail-oriented, organized, and dedicated to providing the best possible travel experience for my clients."""),
                goal=dedent(f"""Provide detailed information and insights about each city, including top attractions, local cuisine, and cultural experiences."""),
                tools=[SearchTools.search_internet],
                verbose=True,
                llm=self.OpenAIGPT4,
            )
