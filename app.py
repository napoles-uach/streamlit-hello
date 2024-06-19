import streamlit as st
import os

# Path del archivo donde se guardarán los mensajes
FILE_PATH = 'messages.txt'

def save_message(message):
    """Guarda el mensaje en el archivo."""
    with open(FILE_PATH, 'a') as file:
        file.write(message + '\n')

def get_messages():
    """Obtiene todos los mensajes guardados en el archivo."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        messages = file.readlines()
    return [msg.strip() for msg in messages]

def main():
    st.title('Streamlit Hello')
    
    # Campo de chat para escribir un mensaje
    prompt = st.chat_input("Escribe tu comentario")
    if prompt:
        save_message(prompt)
        st.success('Mensaje enviado!')

    # Mostrar todos los mensajes
    st.subheader('Mensajes:')
    messages = get_messages()
    for msg in messages:
        st.text(msg)

if __name__ == '__main__':
    main()
