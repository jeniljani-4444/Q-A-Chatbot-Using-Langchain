from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
load_dotenv()


class Chatbot:
    def __init__(self):
        self.open_api_key = os.getenv("OPENAI_API_KEY")
        self.chat = ChatOpenAI(openai_api_key=os.getenv("openai_key"),temperature=0.7)

    def get_response(self,question):
        if "flowmessages" not in st.session_state:
            st.session_state["flowmessages"] = [
                SystemMessage(content="You are a Data Science assistant AI ")
            ]

        st.session_state['flowmessages'].append(HumanMessage(content=question))
        answer = self.chat(st.session_state["flowmessages"])
        st.session_state["flowmessages"].append(AIMessage(content=answer.content))
        return answer.content

    def streamlit_app(self):
        st.set_page_config(page_title="Q&A Chatbot 🤖")
        st.title("Q&A Conversational Chatbot 🤖")

        input_text = st.text_input("Input:",key="input")
        response = self.get_response(input_text)

        btn = st.button("Submit")

        if btn:
            st.subheader("The AI Response:")
            st.write(response)

    

if __name__ == "__main__":
    app = Chatbot()
    app.streamlit_app()