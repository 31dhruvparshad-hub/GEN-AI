from langchain_openai import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    api_key="ENTER THE API KEY"

response = llm.invoke(
    "TELL ME THE NAME OF THE SPECIAL FORCE UNIT OF INDIAN NAVY"
)

print(response)
