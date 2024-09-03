import chainlit as cl
from llm.agent import agent
from typing import Dict, Optional
from literalai import LiteralClient


client = LiteralClient()
client.instrument_openai()


@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    return default_user


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")
    response = agent.stream_chat(message.content)

    for token in response.response_gen:
        await msg.stream_token(token)

    await msg.update()
