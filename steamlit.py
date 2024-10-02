# pip install streamlit langchain lanchain-openai

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


def get_response(user_input):
    return """
    lol, I don't have tools yet to this this action 🥺 \n
    please join ***emnify Hackathon*** to provide me with tools to do it \n
    challenge accepted 🧑‍💻 ?
    """


# app config
st.set_page_config(page_title="Emnify Bolt ⚡", page_icon="⚡")
st.title("Bolt⚡")
st.markdown("lighting bolt-fast, powerful emnify  AGI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hi there, I see you have a new SIM Batch, do you want me to create sim and device for it?"),

    ]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("App Token")

if website_url is None or website_url == "":
    st.info("Please emnify app token")

else:
    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)