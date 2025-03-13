import streamlit as st

class ChatUI:
    def __init__(self, title="Chat Interface"):
        self.title = title
        self.chat_history = []

    def display_title(self):
        st.title(self.title)

    def add_message(self, sender, message):
        self.chat_history.append({"sender": sender, "message": message})
        self.display_chat()

    def display_chat(self):
        st.write("---")
        for chat in self.chat_history:
            sender, message = chat["sender"], chat["message"]
            st.markdown(f"**{sender}:** {message
