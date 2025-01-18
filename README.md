# **Cohere AI Assistant**

### **Overview**

The **Cohere AI Assistant** is a chatbot powered by Cohere's popular **"command-xlarge"** language model. It allows users to interact with a conversational agent that can generate responses based on their inputs. The application is built using **Streamlit** and provides a clean and user-friendly interface for interacting with the model.

### **Technologies Used**
- **Cohere**: Used for generating text-based responses. Cohere provides advanced language models capable of understanding and generating human-like responses.
- **Streamlit**: A Python framework that allows for the rapid creation of interactive web applications. In this project, Streamlit is used to create the interface and manage the flow of the chat.

### **Key Features**
1. **User-Friendly Interface**: A clean chat interface built with Streamlit where users can interact with the assistant.
2. **Custom Styling**: The interface has custom CSS for a professional appearance, including message bubbles with shadows and rounded corners.
3. **Session State Management**: The session state stores the chat history, ensuring that the conversation persists as the user interacts with the assistant.
4. **API Integration**: Cohere's **"command-xlarge"** model is used to generate responses based on the user's input.

### **Functionality**

- **User Input**: The user enters a message via a text input field. The message is added to the chat history and sent to the Cohere API for processing.
- **Cohere Response**: The assistant generates a response using the `cohere_client.generate` method, with parameters like `max_tokens` (limit the response length) and `temperature` (controls the randomness of responses).
- **Display Chat**: The conversation history is displayed in reverse order, with the most recent message at the top. Custom CSS is applied to differentiate between user and assistant messages.

### **Code Walkthrough**

1. **Setting up Cohere API**:
    - The API key is set to authenticate the connection with Cohere's API service.
    - The model used for text generation is `command-xlarge`, which is one of the most popular models in the Cohere suite.

    ```python
    API_KEY = "your_api_key"
    cohere_client = cohere.Client(API_KEY)
    ```

2. **Custom CSS for UI**:
    - The chat interface is styled with CSS to create professional-looking message bubbles with shadows and rounded corners.

    ```python
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
    ```

3. **Chat History Management**:
    - The `st.session_state` is used to store chat history and preserve the conversation across user inputs. This is critical to maintain the flow of the chat, so the assistant can respond appropriately.

    ```python
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    ```

4. **Generating Responses**:
    - The user's input is sent to Cohere's model, and a response is generated. If the request is successful, the assistant's response is appended to the chat history.

    ```python
    response = cohere_client.generate(
        model="command-xlarge",
        prompt=user_input,
        max_tokens=150,
        temperature=0.7,
        stop_sequences=["\n", "User:", "Assistant:"]
    )
    ```

5. **Displaying the Chat**:
    - The chat history is displayed in reverse order to show the most recent message at the top. This ensures that the conversation flows as expected.

    ```python
    for message in reversed(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(f'<div class="user-msg">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">{message["content"]}</div>', unsafe_allow_html=True)
    ```

### **Running the Application**

1. Install the required dependencies:

    ```bash
    pip install streamlit cohere
    ```

2. Save the Python script (e.g., `app.py`).

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Open the app in your browser and start chatting with the assistant!

### **Troubleshooting**

- Ensure that you have a valid API key from Cohere. You can sign up for access on their [website](https://cohere.ai/).
- If you experience errors related to missing dependencies, install them using `pip install streamlit cohere`.

### **Conclusion**

The **Cohere AI Assistant** project demonstrates how to integrate a powerful AI model with a Streamlit-based frontend to create an interactive chatbot. With this project, you can easily customize the assistant for different use cases or deploy it for various conversational tasks.
