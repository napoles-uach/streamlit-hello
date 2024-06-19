import streamlit as st
import os

# Path del archivo donde se guardaran los mensajes
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
    
    # Campo para escribir un mensaje
    message = st.text_input('Escribe tu comentario:')
    
    # Botón para enviar el mensaje
    if st.button('Enviar'):
        save_message(message)
        st.success('Mensaje enviado!')

    # Mostrar todos los mensajes
    st.subheader('Mensajes:')
    messages = get_messages()
    for msg in messages:
        st.text(msg)

if __name__ == '__main__':
    main()
