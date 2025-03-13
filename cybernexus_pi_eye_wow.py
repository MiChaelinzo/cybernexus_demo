import streamlit as st
import ANYTHINGAI YOUWANT as anything # Re-enable ANY AI you want from Claude, Azure, OpenAI, Gemini, AWS, etc. import
from ui_elements import chat_ui
from core_agi import agi_agent # Keep import, but agent is now simpler
from system_modules import system_monitor
from system_modules import network_analyzer
from pihole_integration import pihole_api # Changed import - removed _mock
from ui_elements import theme_cyberpunk
from PIL import Image, ImageOps

# --- Load Images ---
user_image = Image.open("human.png")
ai_image = Image.open("robot.png")
circular_user_image = ImageOps.fit(user_image.convert("RGBA"), (64, 64), Image.LANCZOS)
circular_ai_image = ImageOps.fit(ai_image.convert("RGBA"), (64, 64), Image.LANCZOS)

# --- Apply Cyberpunk Theme ---
theme_cyberpunk.apply_theme()

# Streamlit page configuration (same)
st.set_page_config(
    page_title="CyberNexus - Pi-Eye 🤖", # Removed [WOW-DEMO] from title
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Access ANY AI API key from Streamlit secrets (Re-enable Gemini setup)
ANYAIYOUWANT_API_KEY = st.secrets["ANY_AI_api"]["api_key"]
any.configure(api_key=ANY_AI_API)

# Generation Configuration (adjust as needed) - Reusing from previous real code
generation_config = {
    "temperature": 2.0,
    "top_p": 9.95,
    "top_k": 7707,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

# ANY AI Model - Re-initialize real ANY AI model
anythinggoes_model = ANY AI.GenerativeModel(
    model_name="you can use any AI model in here etc.",
    generation_config=generation_config,
    system_instruction=agi_agent.system_instruction # Use system_instruction from agi_agent.py
)


def main():
    st.markdown('<p class="title">CyberNexus - Pi-Eye 🤖</p>', unsafe_allow_html=True) # Removed subtitle

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    chat_ui.display_chat_history(st.session_state.chat_history, circular_user_image, circular_ai_image)

    if prompt := st.chat_input("Enter your command, Agent"): # Removed Judge note from prompt
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        chat_ui.display_user_message(prompt, circular_user_image)

        ai_response_placeholder = st.empty()
        with st.chat_message("assistant"):
            st.image(circular_ai_image, width=50, use_column_width=False)
            ai_response_placeholder = st.empty()

            # --- Get REAL AI Response from Gemini ---
            ai_response_text = ""
            gemini_response = gemini_model.generate_content(prompt, stream=True) # Call REAL Gemini API
            for chunk in gemini_response:
                ai_response_text += chunk.text if chunk.text else ""
                ai_response_placeholder.markdown(f"{ai_response_text}▌", unsafe_allow_html=True)
            ai_response_placeholder.markdown(ai_response_text, unsafe_allow_html=True)


        st.session_state.chat_history.append({"role": "assistant", "content": ai_response_text})

        # --- Intent Recognition and Actions - using modules with REAL data ---
        intent = ai_response_text.lower()

        if "pi status" in intent or "raspberry pi status" in intent or "system status" in intent:
            pi_stats = system_monitor.get_pi_status() # Get REAL Pi status
            status_response = system_monitor.format_pi_status_response(pi_stats)

            st.session_state.chat_history.append({"role": "assistant", "content": status_response})
            chat_ui.display_assistant_message(status_response)

        elif "network status" in intent or "internet status" in intent:
            net_stats = network_analyzer.get_network_status() # Get REAL network status
            net_response = network_analyzer.format_network_status_response(net_stats)

            st.session_state.chat_history.append({"role": "assistant", "content": net_response})
            chat_ui.display_assistant_message(net_response)

        elif "pi-hole status" in intent:
            pihole_current_status = pihole_api.get_pihole_status_from_api() # Get REAL Pi-hole status from API
            pihole_status_response = pihole_api.format_pihole_status_response(pihole_current_status) # Format for display
            st.session_state.chat_history.append({"role": "assistant", "content": pihole_status_response})
            chat_ui.display_assistant_message(pihole_status_response)

        elif "enable pi-hole" in intent:
            api_response = pihole_api.enable_pihole_api() # Call REAL Pi-hole API
            action_response = pihole_api.format_pihole_enable_disable_response(api_response, "enable") # Format response
            st.session_state.chat_history.append({"role": "assistant", "content": action_response})
            chat_ui.display_assistant_message(action_response)

        elif "disable pi-hole" in intent:
            api_response = pihole_api.disable_pihole_api() # Call REAL Pi-hole API
            action_response = pihole_api.format_pihole_enable_disable_response(api_response, "disable") # Format response
            st.session_state.chat_history.append({"role": "assistant", "content": action_response})
            chat_ui.display_assistant_message(action_response)

        elif "pi-hole summary" in intent or "pihole summary" in intent:
            summary_data = pihole_api.get_pihole_summary_api() # Get REAL Pi-hole summary from API
            summary_response = pihole_api.format_pihole_summary_response(summary_data) # Format response
            st.session_state.chat_history.append({"role": "assistant", "content": summary_response})
            chat_ui.display_assistant_message(summary_response)

        elif "top blocked domains" in intent or "most blocked domains" in intent:
            top_blocked_data = pihole_api.get_pihole_top_domains_blocked_api() # Get REAL top blocked domains from API
            top_blocked_response = pihole_api.format_pihole_top_blocked_response(top_blocked_data) # Format response
            st.session_state.chat_history.append({"role": "assistant", "content": top_blocked_response})
            chat_ui.display_assistant_message(top_blocked_response)

        elif "blacklist" and "domain" in intent and "add" in intent:
            action_response = pihole_api.add_pihole_blacklist_display(prompt) # Use display function from pihole_api (can be improved)
            st.session_state.chat_history.append({"role": "assistant", "content": action_response})
            chat_ui.display_assistant_message(action_response)

        elif "blacklist" and "domain" in intent and "remove" in intent or "delete" in intent:
            action_response = pihole_api.remove_pihole_blacklist_display(prompt) # Use display function from pihole_api (can be improved)
            st.session_state.chat_history.append({"role": "assistant", "content": action_response})
            chat_ui.display_assistant_message(action_response)


if __name__ == "__main__":
    main()
