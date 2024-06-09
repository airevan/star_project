import streamlit as st
import constants
import requests

st.set_page_config(
    page_title=constants.PAGE_TITLE,
    layout="wide",
)
st.header(constants.PAGE_HEADER)

with st.sidebar:
    st.header("Welcome!!!")
    st.subheader("Ask me some questions")
    if st.button(constants.SAMPLE_MESSAGE_1):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": constants.SAMPLE_MESSAGE_1,
            }
        )

    if st.button(constants.SAMPLE_MESSAGE_2):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": constants.SAMPLE_MESSAGE_2,
            }
        )

    if st.button(constants.SAMPLE_MESSAGE_3):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": constants.SAMPLE_MESSAGE_3,
            }
        )

    if st.button(constants.SAMPLE_MESSAGE_4):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": constants.SAMPLE_MESSAGE_4,
            }
        )

if "messages" not in st.session_state.keys():
    st.session_state["messages"] = list()

if prompt := st.chat_input("Ask me about the vulnerabilities of your assets"):
    st.session_state["messages"].append({"role": "user", "content": prompt})

for message in st.session_state["messages"]:
    with st.chat_message(message["role"], avatar=constants.AVATAR_MAP[message["role"]]):
        st.write(message["content"])


if st.session_state["messages"] and st.session_state["messages"][-1]["role"] == "user":
    last_message = st.session_state["messages"][-1]
    payload = {"messages": [last_message]}

    with st.spinner("Thinking..."):
        with st.chat_message("assistant", avatar=constants.AVATAR_MAP["assistant"]):
            answer_from_llm = "I am sure you will find answer on your own"
            st.write(answer_from_llm)

        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": answer_from_llm,
            }
        )
    # with requests.post(constants.CHAT_URL, json=payload, stream=True) as response:
    #     for chunk in response.iter_lines():
    #         chunk_text = chunk.decode("utf-8")
    #         print(chunk_text)
