import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

# Setup the OpenAI client to use the Azure API
load_dotenv(override=True)
API_HOST = os.getenv("API_HOST")

if API_HOST == "azure":

    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        openai_api_version=os.getenv("AZURE_OPENAI_VERSION"),
        api_key=os.getenv("AZURE_AI_PROJECT_API_KEY")
    )

prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{input}")]
)
chain = prompt | llm
response = chain.invoke({"input": "please tell me about the online esports competitive game of valorant."})

print(f"Response from {API_HOST}: \n")
print(response.content)
