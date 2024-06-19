import streamlit as st
import os
from rich import print

# Path of the file where messages will be stored
FILE_PATH = 'messages.txt'
MAX_MESSAGES = 10  # Maximum number of messages to save

def save_message(nickname, message):
    """Saves the message in the file along with the user's nickname."""
    full_message = f"{nickname}: {message}" if nickname else message
    messages = get_messages()
    messages.append(full_message)
    # Keep only the last 10 messages
    messages = messages[-MAX_MESSAGES:]
    with open(FILE_PATH, 'w') as file:
        for msg in messages:
            file.write(msg + '\n')

def get_messages():
    """Retrieves all messages saved in the file."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        messages = file.readlines()
    return [msg.strip() for msg in messages]

def clear_messages():
    """Clears all messages from the file."""
    open(FILE_PATH, 'w').close()

def main():
    st.title('Say Hello 👋')
    
    # Input for nickname in the sidebar
    nickname = st.sidebar.text_input("Enter your name or nickname (optional):")
    
    # Chat input to write a message
    prompt = st.chat_input("Write your comment")
    if prompt:
        print(nickname, prompt)
        save_message(nickname, prompt)
        st.success('Message sent!')

    # Button to clear all messages
    if st.button('Clear all messages'):
        clear_messages()
        st.success('All messages have been cleared.')

    # Display all messages
    st.subheader('Messages:')
    messages = get_messages()
    
    # Create a style block
    st.markdown(
        """
        <style>
        .message {
            color: navy;
            background-color: #f0f2f6;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ccc;
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use HTML to display the messages
    for msg in messages:
        st.markdown(f'<div class="message">{msg}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

