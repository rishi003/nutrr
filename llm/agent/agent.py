from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI


__all__ = ["agent"]


llm = OpenAI()

agent = OpenAIAgent.from_llm(llm=llm)
