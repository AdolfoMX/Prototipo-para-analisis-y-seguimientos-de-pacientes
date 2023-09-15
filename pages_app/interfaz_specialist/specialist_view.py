import streamlit as st
import streamlit_authenticator as stauth

from pages_app.interfaz_specialist.form_slsm import form_main
from pages_app.interfaz_specialist.progress_record import progress_record_main
from streamlit_option_menu import option_menu


def specialist_view_main():
    with st.sidebar:
        
        # Inicio de código
        st.markdown(
            """
            <style>
                [data-testid=stSidebar] [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-top: -24%;
                    margin-bottom: 2%;
                    margin-left: auto;
                    margin-right: auto%;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.image(".\\images\\mostrador.png", width=180, use_column_width=False)
        
        selectd = option_menu(
            menu_title="Menú principal",
            options=["Inicio", "Pacientes", "Cuestionario SLSM", "Registro de avances", "Visualizaciones"],
            icons=["house", "people", "file-medical", "percent", "bar-chart"]
        )           
        
        # Salir sesión
        st.session_state["rol_logout"].logout('Salir de sesión', 'main')
    
    # Secciones
    if selectd == "Inicio":        
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Pacientes":
        st.write(f"Haz seleccionado {selectd}")
        
    if selectd == "Cuestionario SLSM":
        form_main()

    if selectd == "Registro de avances":
        progress_record_main()

    if selectd == "Visualizaciones":
        st.write(f"Haz seleccionado {selectd}")