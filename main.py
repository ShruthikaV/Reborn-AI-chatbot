import streamlit as st
import time
import backend_module

# Ensure page config is the first Streamlit command
st.set_page_config(page_title="Reborn - Patient Query Bot", page_icon="💬", layout="wide")

with st.sidebar:
    st.header("ℹ️ How to Use")
    st.write("💡 Ask questions about addiction help, treatments, or coping strategies.")
    st.write("📝 Your conversation history is saved in this session.")
    st.write("🔄 Refreshing will clear the chat history.")

st.sidebar.markdown("<br>" * 8, unsafe_allow_html=True)  # Push contact details lower

# Sidebar for Contact Details
st.sidebar.title("📞 Contact Details")
st.sidebar.write("**Support Email:** support@example.com")
st.sidebar.write("**Helpline:** +1-800-123-4567")
st.sidebar.write("**Website:** [Visit Us](https://www.example.com)")
st.sidebar.write("**Office Hours:** 9 AM - 5 PM (Mon-Fri)")

# Inject CSS for custom chat styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }

        .chat-container {
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            max-width: 80%;
            word-wrap: break-word;
        }

        /* User messages (Gray) */
        .user-message {
            background-color: #d3d3d3;
            color: black;
            padding: 10px;
            border-radius: 10px;
            text-align: left;
            display: inline-block;
            max-width: 80%;
        }

        /* Assistant messages (Indigo) */
        .assistant-message {
            background-color: #3f51b5;
            color: white;
            padding: 10px;
            border-radius: 10px;
            text-align: left;
            display: inline-block;
            max-width: 80%;
        }

        .message-container {
            display: flex;
            justify-content: flex-start;
        }

        .user-message-container {
            display: flex;
            justify-content: flex-end;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to generate streamed response
def response_generator(prompt):
    response = backend_module.GenerateResponse(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
    return response  # Ensure the final response is returned

st.title("💬 Reborn - Patient Query Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message-container"><div class="chat-container user-message">{message["content"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-container"><div class="chat-container assistant-message">{message["content"]}</div></div>', unsafe_allow_html=True)

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    st.markdown(f'<div class="user-message-container"><div class="chat-container user-message">{prompt}</div></div>', unsafe_allow_html=True)

    # Generate response
    with st.spinner("Thinking..."):
        response_text = "".join(response_generator(prompt))

    # Display assistant response
    st.markdown(f'<div class="message-container"><div class="chat-container assistant-message">{response_text}</div></div>', unsafe_allow_html=True)

    # Add response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------




# import streamlit as st
# import time
# import backend_module

# st.title("💬 Patient Addiction Query Bot")

# st.sidebar.markdown("<br>" * 17, unsafe_allow_html=True)  # Adjust number to move it further down

# # Sidebar for Contact Details
# st.sidebar.title("📞 Contact Details")
# st.sidebar.write("*Support Email:* support@example.com")
# st.sidebar.write("*Helpline:* +1-800-123-4567")
# st.sidebar.write("*Website:* [Visit Us](https://www.example.com)")
# st.sidebar.write("*Office Hours:* 9 AM - 5 PM (Mon-Fri)")



# # Set page config for a better layout
# st.set_page_config(page_title="Patient Addiction Query Bot", page_icon="💬", layout="wide")

# # Custom CSS for chat styling
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #f0f2f6;
#         }
        
#         /* Chat container */
#         .chat-container {
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#             max-width: 80%;  
#             padding: 10px 15px;
#             border-radius: 10px;
#             word-wrap: break-word;
#         }

#         /* User messages (Gray) */
#         .user-message {
#             background-color: #d3d3d3;  /* Light Gray */
#             color: black;
#             padding: 10px;
#             border-radius: 10px;
#             text-align: left;
#             display: inline-block;
#             max-width: 80%;
#             word-wrap: break-word;
#         }

#         /* Chatbot messages (Indigo) */
#         .assistant-message {
#             background-color: #3f51b5;  /* Indigo */
#             color: white;
#             padding: 10px;
#             border-radius: 10px;
#             text-align: left;
#             display: inline-block;
#             max-width: 80%;
#             word-wrap: break-word;
#         }

#         /* Message container */
#         .message-container {
#             display: flex;
#             justify-content: flex-start;  /* Align messages to the left */
#         }

#         /* Align user messages to the right */
#         .user-message-container {
#             display: flex;
#             justify-content: flex-end;
#         }

#     </style>
#     """,
#     unsafe_allow_html=True
# )


# st.title("💬 Patient Addiction Query Bot")

# # Sidebar for instructions
# with st.sidebar:
#     st.header("ℹ️ How to Use")
#     st.write("💡 Ask questions about addiction help, treatments, or coping strategies.")
#     st.write("📝 Your conversation history is saved in this session.")
#     st.write("🔄 Refreshing will clear the chat history.")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history
# for message in st.session_state.messages:
#     role_class = "user-message" if message["role"] == "user" else "assistant-message"
#     with st.chat_message(message["role"]):
#         st.markdown(f"<div class='{role_class}'>{message['content']}</div>", unsafe_allow_html=True)

# # Function to generate streaming response
# def response_generator(prompt):
#     response = backend_module.GenerateResponse(prompt)
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# # Accept user input
# if prompt := st.chat_input("Type your message here..."):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
    
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(f"<div class='user-message'>{prompt}</div>", unsafe_allow_html=True)

#     # Display assistant response with a loading animation
#     with st.chat_message("assistant"):
#         response_container = st.empty()
#         response = "".join(response_generator(prompt))
#         response_container.markdown(f"<div class='assistant-message'>{response}</div>", unsafe_allow_html=True)
    
#     # Save response in session state
#     st.session_state.messages.append({"role": "assistant", "content": response})
