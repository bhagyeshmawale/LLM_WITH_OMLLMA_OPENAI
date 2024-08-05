from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.vectorstores import FAISS

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] ="true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

LANGCHAIN_TRACING_V2= "true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT="tutorial1"

# api_key = os.getenv("LANGCHAIN_API_KEY")
api_key = LANGCHAIN_API_KEY
if api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = api_key
else:
    raise ValueError("LANGCHAIN_API_KEY environment variable is not set.")

## prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system"," you are a helpful assistant. Please response to the user  queries"),
        ("user","question:{question}")
    ]
)

## streamlit framwork

st.title('langchain chatbot')
input_text = st.text_input("Search the topic you want")

llm = ChatOpenAI(model='gpt-3.5-turbo')                     
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

