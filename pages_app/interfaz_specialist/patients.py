import streamlit as st
from streamlit_option_menu import option_menu

def patients_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.title("Información de pacientes")
        
        selectd = option_menu(
            menu_title=None,
            options=["Búsqueda de pacientes"],
            orientation="horizontal"
        )
        
        with st.form("Buscar pacientes", clear_on_submit=True):    
            search_val = st.text_input("Escriba el nombre del paciente:")
            submitted = st.form_submit_button("Buscar")
        
            if submitted:
                st.write("Accion aceptada")