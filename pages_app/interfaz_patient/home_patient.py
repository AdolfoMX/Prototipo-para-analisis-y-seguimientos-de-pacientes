import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

def home_patient():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
            """, unsafe_allow_html=True
        )
        
        st.title("Inicio")
        st.subheader("", divider="orange")
        
        text_colum1, image_column2 = st.columns(2)

        with text_colum1:
            st.write(
            """
            En *"Salud Latina Sin Medicina"* creemos que el estilo de vida influye más que cualquier medicamento en nuestra salud. Pensamos que para mejorar no siempre es necesario recurrir a los medicamentos, sino que queremos brintarte la alternativa de progresar a través de un espacio donde podrás encontrar recursos y apoyo para abordar tu salud de manera equilibrada y próspera.
            
            Adelantate, explora y mejora. Estamos emocionados de tenerte con nosotros mientras trabajamos en conjunto para una vida más saludable, fuerte y feliz.
            """
        )
        st.write(f"¡Bienvenido, :blue[{st.session_state.name}] al programa Salud Latina Sin Medicina! Tu salud, tu bienestar.")

        with image_column2:
            with open("images/doctor.json", "r",errors='ignore') as f:
                data = json.load(f)
        
            st_lottie(data)