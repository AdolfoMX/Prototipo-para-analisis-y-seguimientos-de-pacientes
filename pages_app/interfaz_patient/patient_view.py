import streamlit as st

from pages_app.interfaz_patient.form_slsm import form_main
from streamlit_option_menu import option_menu

def patient_view_main():
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
        
        st.image(".\\images\\chat.png", width=180, use_column_width=False)
        
        selectd = option_menu(
            menu_title="Menú principal",
            options=["Inicio", "Información", "Cuestionario SLSM", "Registro de avances", "Visualizaciones"],
            icons=["house", "file-earmark-person", "file-medical", "percent", "bar-chart"]
        )           
        
        # Salir sesión
        st.session_state["rol_logout"].logout('Salir de sesión', 'main')
    
    # Secciones
    if selectd == "Inicio":        
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Pacientes":
        st.write(f"Haz seleccionado {selectd}")
        
    if selectd == "Cuestionario SLSM":
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Registro de avances":
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Visualizaciones":
        st.write(f"Haz seleccionado {selectd}")