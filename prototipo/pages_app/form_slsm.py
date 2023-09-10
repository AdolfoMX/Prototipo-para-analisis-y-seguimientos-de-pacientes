import streamlit as st
from streamlit_option_menu import option_menu

def form_main():
    
    with st.container():
        
        # Inicio de código
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -5rem;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.title("Registro de datos")
        
        selectd = option_menu(
            menu_title=None,
            options=["Historial médico", "Hoja de evolución"],
            orientation="horizontal"
        )
        
        # Secciones
        if selectd == "Historial médico":
            
            with st.form("Historial médico", clear_on_submit=True):
                
                # Sección 1 de preguntas
                st.subheader("Sección 1")
                col1_sec1, col2_sec1 = st.columns(2)
                
                with col1_sec1:
                    name = st.text_input("Nombre")
                    email = st.text_input("Correo electrónico")
                    age = st.number_input('Edad', min_value=1, max_value=110, step=1)
                
                with col2_sec1:
                    last_name = st.text_input("Apellidos")
                    number_phone = st.text_input("Número de teléfono")
                    genre = st.radio("Género", options=["Masculino", "Femenino", "Otro"], horizontal=True)
                
                
                st.divider()
                
                # Sección 2 de preguntas
                st.subheader("Sección 2")
                
                submitted = st.form_submit_button("Enviar")
                
            
        
        if selectd == "Hoja de evolución":
            st.write(f"Seleccionaste: {selectd}")
        
