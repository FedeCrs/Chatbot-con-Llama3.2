import streamlit as st
import requests
from PIL import Image   # Cargar la imagen como base64
import base64

# CSS personalizado para la imagen de fondo
def add_background(image_file, opacity=0.9):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, {1 - opacity}), rgba(255, 255, 255, {1 - opacity})),
                        url(data:image/png;base64,{image_file});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .text-container {{
            background-color: rgba(255, 255, 255, 1); /* Fondo oscuro detrás del texto */
            padding: 10px; /* Espaciado interno */
            border-radius: 10px; /* Bordes redondeados */
            color: white; /* Texto blanco */ 
            font-weight: bold; /* Negrita */
            text-shadow: 2px 2px 6px rgba(255, 255, 255, 1); /* Sombra fuerten*/
        }}
        .stButton>button {{
            background-color: #1E90FF; /* Color azul para botones */
            color: white;
            border-radius: 5px;
            font-weight: bold;         /* Negrita en botones */
            box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Sombra en botón */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Cargar la imagen de fondo
image_base64 = load_image_as_base64("llamaImage.webp")
add_background(image_base64, opacity=0.4)

st.title('Agente de apoyo con IA 🤖 para trabajo interno, seguro y eficaz')
st.markdown("Escribe un mensaje y envíalo para obtener una respuesta del servidor")

# Entrada de texto para el usuario
user_input = st.text_input("Escribe tu mensaje:", "")


# Botón para enviar el mensaje
if st.button('Enviar'):
    if user_input:
        try:
            # Enviar el mensaje al servidor Flask
            response = requests.post('http://127.0.0.1:5000/chat', json={'message': user_input})
            
            if response.status_code == 200:
                # Mostrar la respuesta del servidor
                data = response.json()
                st.text_area('Respuesta:', value=data.get('response', 'Sin respuesta'), height=200)
            else:
                # Mostrar el mensaje de error
                st.error(f"Error en el servidor: {response.json().get('error', 'Sin detalles')}")
        except Exception as e:
            st.error(f"Error al conectar con el servidor: {e}")
    else:
        st.warning('Por favor, escribe un mensaje antes de enviar.') 

# Información adicional o pie de  página
st.markdown("---")
st.caption("Desarrollado por Fede. Basado en IA con Flask y Streamlit")
                                                        