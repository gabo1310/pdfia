import os
from langchain_anthropic import ChatAnthropic

def build_llm_clau(chat_args, model_name):

    api_key = os.getenv('ANTHROPIC_API_KEY')  

    if api_key is None:
        raise ValueError("API key is not set in the environment variables.")

    return ChatAnthropic(
        streaming=chat_args.streaming,
        model_name=model_name
    )