import streamlit as st
import os
import time

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

def check_for_changes():
    """Revisa el archivo para cambios y rerun si es necesario."""
    last_mod_time = st.session_state.get('last_mod_time', None)
    current_mod_time = os.path.getmtime(FILE_PATH) if os.path.exists(FILE_PATH) else None
    
    if last_mod_time is not None and last_mod_time != current_mod_time:
        st.experimental_rerun()

    st.session_state['last_mod_time'] = current_mod_time

def main():
    st.title('Streamlit Hello')
    
    # Entrada para nickname en la barra lateral
    nickname = st.sidebar.text_input("Ingresa tu nombre o nickname (opcional):")
    
    # Campo de chat para escribir un mensaje
    prompt = st.chat_input("Escribe tu comentario")
    if prompt:
        save_message(nickname, prompt)
        st.success('Mensaje enviado!')

    # Botón para borrar todos los mensajes
    if st.button('Borrar todos los mensajes'):
        clear_messages()

    # Chequear por cambios en el archivo antes de mostrar mensajes
    check_for_changes()

    # Mostrar todos los mensajes
    st.subheader('Mensajes:')
    messages = get_messages()
    for msg in messages:
        st.text(msg)

if __name__ == '__main__':
    main()
