from langchain_core.tools import tool

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic}"
)

chain = prompt | llm

@tool
def multiply(a:int,b:int) -> int:
    return a * b

llm_with_tools=llm.bind_tools([multiply])