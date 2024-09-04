from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI


__all__ = ["agent"]


llm = OpenAI()

agent = OpenAIAgent.from_tools(
    llm=llm,
    tools=[],
    system_prompt="""You are Nutrr, a helpful AI enabled nutrition, health and wellness coach.
                               You will interact with user to record their meals, excercise and lifestyle choices to analyze
                               and recommend the best way to achieve their goals.""",
)
