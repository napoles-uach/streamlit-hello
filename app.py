import streamlit as st
import os

# Path del archivo donde se guardarán los mensajes
FILE_PATH = 'messages.txt'
MAX_MESSAGES = 10  # Máximo número de mensajes a guardar

def save_message(nickname, message):
    """Guarda el mensaje en el archivo junto con el nickname del usuario."""
    full_message = f"{nickname}: {message}" if nickname else message
    messages = get_messages()
    messages.append(full_message)
    # Mantener solo los últimos 10 mensajes
    messages = messages[-MAX_MESSAGES:]
    with open(FILE_PATH, 'w') as file:
        for msg in messages:
            file.write(msg + '\n')

def get_messages():
    """Obtiene todos los mensajes guardados en el archivo."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        messages = file.readlines()
    return [msg.strip() for msg in messages]

def clear_messages():
    """Borra todos los mensajes del archivo."""
    open(FILE_PATH, 'w').close()

def main():
    st.title('Streamlit Hello')
    
    # Entrada para nickname en la barra lateral
    nickname = st.sidebar.text_input("Ingresa tu nombre o nickname (opcional):")
    
    # Campo de chat para escribir un mensaje
    prompt = st.chat_input("Escribe tu comentario")
    if prompt:
        save_message(nickname, prompt)
        st.success('Mensaje enviado!')
        st

