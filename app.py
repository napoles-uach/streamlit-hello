import streamlit as st
import os

# Path del archivo donde se guardarán los mensajes
FILE_PATH = 'messages.txt'
MAX_MESSAGES = 10  # Máximo número de mensajes a guardar

def save_message(message):
    """Guarda el mensaje en el archivo y asegura que no se excedan los 10 mensajes."""
    messages = get_messages()
    messages.append(message)
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
    
    # Campo de chat para escribir un mensaje
    prompt = st.chat_input("Escribe tu comentario")
    if prompt:
        save_message(prompt)
        st.success('Mensaje enviado!')

    # Botón para borrar todos los mensajes
    if st.button('Borrar todos los mensajes'):
        clear_messages()
        st.success('Todos los mensajes han sido borrados.')

    # Mostrar todos los mensajes
    st.subheader('Mensajes:')
    messages = get_messages()
    for msg in messages:
        st.text(msg)

if __name__ == '__main__':
    main()
