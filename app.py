import cohere
import streamlit as st

# Set your Cohere API token
API_KEY = "r7zMPdYiqCr9CN4pCs8EyLwNLVJynXCNxyew7IVR"
cohere_client = cohere.Client(API_KEY)

st.title("Cohere AI Assistant")
st.write("A chatbot powered by Cohere's most popular model.")

# Custom CSS for a professional chat interface
st.markdown("""
    <style>
    .user-msg {
        background-color: #D1F7FF;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        margin-left: 0;
        margin-right: auto;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .assistant-msg {
        background-color: #F4F6F9;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        margin-left: auto;
        margin-right: 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize the session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    # First append the user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.spinner("Generating response..."):
        try:
            # Use Cohere's popular model, "command-xlarge"
            response = cohere_client.generate(
                model="command-xlarge",
                prompt=user_input,
                max_tokens=150,
                temperature=0.7,
                stop_sequences=["\n", "User:", "Assistant:"]
            )
            # Get the assistant's response
            response_text = response.generations[0].text.strip()
            # Append the assistant's response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display chat history in reverse order with custom styles
chat_container = st.container()
with chat_container:
    # Reverse the chat history to show the most recent messages at the top
    for message in reversed(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(f'<div class="user-msg">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">{message["content"]}</div>', unsafe_allow_html=True)
