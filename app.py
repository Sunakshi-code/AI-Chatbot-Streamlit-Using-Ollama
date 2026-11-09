
import streamlit as st
import ollama

# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

MODEL_NAME = "qwen2.5:1.5b"

# 2. CUSTOM CSS - LIGHT & DARK THEME

st.markdown("""
<style>

/* Main Application */
.stApp {
    background: var(--background-color);
    color: var(--text-color);
}

/* Main Content */
[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--secondary-background-color);
    border-right: 1px solid var(--border-color);
}

/* Main Heading */
h1 {
    color: var(--text-color) !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3, p, label {
    color: var(--text-color);
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: var(--secondary-background-color) !important;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}

/* Chat Message Text */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] strong {
    color: var(--text-color) !important;
}

/* Chat Input */
[data-testid="stChatInput"] {
    background: var(--secondary-background-color);
    border: 1px solid var(--border-color);
    border-radius: 16px;
}

/* Input Text */
[data-testid="stChatInput"] textarea {
    color: var(--text-color) !important;
    background: transparent !important;
}

/* Buttons */
.stButton button {
    border-radius: 12px;
    font-weight: 600;
    padding: 10px 15px;
    border: 1px solid var(--border-color);
    transition: all 0.2s ease;
}

/* Button Hover */
.stButton button:hover {
    border-color: var(--primary-color);
    color: var(--primary-color);
}

/* Download Button */
.stDownloadButton button {
    border-radius: 12px;
    font-weight: 600;
}

/* Select Box */
[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: var(--secondary-background-color);
    border-radius: 10px;
    color: var(--text-color);
}

/* Info Message */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: var(--border-color);
}

/* Code Blocks */
[data-testid="stCode"] {
    border-radius: 10px;
}

/* Spinner */
.stSpinner > div {
    border-top-color: var(--primary-color);
}

/* Smooth Appearance */
* {
    transition: background-color 0.2s ease,
                border-color 0.2s ease;
}

</style>
""", unsafe_allow_html=True)


# 3. RESPONSE PERSONALITIES

styles = {
    "Friendly": "Respond in a friendly and conversational way.",

    "Professional": "Respond professionally with clear and structured answers.",

    "Teacher": "Explain concepts step by step using simple language and examples.",

    "Technical": "Provide detailed technical explanations with relevant terminology."
}


# 4. SESSION STATE

if "messages" not in st.session_state:
    st.session_state.messages = []

if "response_style" not in st.session_state:
    st.session_state.response_style = "Friendly"


# 5. SIDEBAR

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.caption("Your Personal AI Chatbot")

    st.divider()

    # AI Model
    st.subheader("AI Model")

    st.code(MODEL_NAME)

    st.divider()

    # Response Personality
    st.subheader("Response Style")

    response_style = st.selectbox(
        "Choose AI Personality",
        list(styles.keys()),
        key="response_style"
    )

    st.divider()

    # New Chat
    if st.button("➕ New Chat", use_container_width=True):

        st.session_state.messages = []
        st.rerun()

    # Chat History
    st.subheader("Chat History")

    if st.session_state.messages:

        st.caption(
            f"{len(st.session_state.messages)} messages in current chat"
        )

    else:

        st.caption("No previous conversations")

    st.divider()

    # Download Chat
    if st.session_state.messages:

        chat_text = ""

        for message in st.session_state.messages:

            role = message["role"].upper()
            content = message["content"]

            chat_text += f"{role}:\n{content}\n\n"

        st.download_button(
            label="⬇️ Download Chat",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain",
            use_container_width=True
        )

    # Clear Chat
    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Powered by Python, Streamlit & Ollama")


# 6. MAIN CHAT INTERFACE

st.title("🤖 AI Chatbot")

st.caption("Your intelligent AI assistant")

st.divider()

# Welcome Message
if not st.session_state.messages:

    st.info(
        "Hello! Welcome to your AI assistant. "
        "Ask me anything!"
    )


# 7. DISPLAY CHAT HISTORY

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# 8. USER INPUT

user_input = st.chat_input(
    "Type your message here..."
)

if user_input:

    # Save User Message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display User Message
    with st.chat_message("user"):

        st.markdown(user_input)

   
    # 9. GENERATE OLLAMA RESPONSE

    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            try:

                # System Instructions
                system_message = {
                    "role": "system",
                    "content": f"""
                    You are an intelligent and helpful AI assistant.

                    Your responsibilities:

                    1. Give clear and accurate answers.
                    2. Use simple language.
                    3. Explain difficult concepts step by step.
                    4. Provide examples whenever useful.
                    5. Organize answers using headings and bullet points.
                    6. Ask for clarification when necessary.

                    Response personality:
                    {styles[response_style]}
                    """
                }

                # Ollama API Call
                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=[
                        system_message,
                        *st.session_state.messages
                    ]
                )

                assistant_response = response["message"]["content"]

                if not assistant_response:
                    assistant_response = (
                        "I couldn't generate a response. Please try again."
                    )

                # Display AI Response
                st.markdown(assistant_response)

                # Save Assistant Message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })

            except Exception as error:

                st.error(
                    "Unable to connect to Ollama. "
                    "Please make sure Ollama is running."
                )

                st.caption(f"Error details: {error}")
