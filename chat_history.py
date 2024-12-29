import os

import openai
from dotenv import load_dotenv

# Setup the OpenAI client to use the Azure API
load_dotenv(override=True)
API_HOST = os.getenv("API_HOST")

if API_HOST == "azure":

    client = openai.AzureOpenAI(
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_AI_PROJECT_API_KEY")
    )
    MODEL_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")

messages = [
    {"role": "system", "content": "I am a Valorant coach who can help you improve in the online game of valorant."},
]

while True:
    question = input("\nYour question: ")
    print("Sending question...")

    messages.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=1,
        max_tokens=4000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    bot_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_response})

    print("Answer: ")
    print(bot_response)
