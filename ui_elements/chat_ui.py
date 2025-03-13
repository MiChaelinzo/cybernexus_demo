"""
Streamlit Chat UI Components Module

This module contains functions to handle the display of chat messages
in the CyberNexus Streamlit application.

For this DEMO, it focuses on basic text-based chat display.

Future enhancements:
- Implement richer chat message formatting (e.g., using markdown, code blocks).
- Add support for different message types (e.g., images, interactive elements).
- Potentially integrate with a UI library for more advanced chat interface features.
"""

import streamlit as st

def display_chat_history(history, user_image, ai_image):
    """Displays the chat history in the Streamlit app."""
    for message in history:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.image(user_image, width=50, use_column_width=False)
            else:
                st.image(ai_image, width=50, use_column_width=False)
            st.markdown(message["content"], unsafe_allow_html=True) # Allow markdown

def display_user_message(prompt, user_image):
    """Displays a user message in the chat UI."""
    with st.chat_message("user"):
        st.image(user_image, width=50, use_column_width=False)
        st.markdown(prompt)

def display_assistant_message(response_content):
    """Displays an assistant message in the chat UI."""
    with st.chat_message("assistant"):
        #st.image(ai_image, width=50, use_column_width=False) # Image moved to main loop for typing effect
        st.markdown(response_content, unsafe_allow_html=True) # Allow markdown
