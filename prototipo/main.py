import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from pages_app.form_slsm import form_main

import time

st.set_page_config(
    page_title="SLSM app",
    page_icon=":hospital:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Autenticación de usuario
names = ["admin"]
usernames = ["admin"]
passwords = ["12345"]
hashed_password = ["$2b$12$nflzQj3nySx8F44R3TGpeO0DoaQraODD5MQrEa.By/Sf9n2Vc9wLK"]


authenticator = stauth.Authenticate(names, usernames, hashed_password, "SLSM app", "auth", cookie_expiry_days=30)

#time.sleep(0.2)

# Inicio de sesión
name, authentication_status, username = authenticator.login("Inicio de sesión", "main")

# Verificación
if st.session_state['authentication_status']:  
    
    time.sleep(0.2)
    
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
        
        st.image(".\\prototipo\\images\\mostrador.png", width=180, use_column_width=False)
        
        selectd = option_menu(
            menu_title="Menú principal",
            options=["Inicio", "Pacientes", "Cuestionario SLSM", "Registro de avances", "Visualizaciones"],
            icons=["house", "people", "file-medical", "percent", "bar-chart"]
        )
        
        # Salir sesión
        authenticator.logout('Logout', 'main')
    
    # Secciones
    if selectd == "Inicio":        
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Pacientes":
        st.write(f"Haz seleccionado {selectd}")
        
    if selectd == "Cuestionario SLSM":
        # st.write(f"Haz seleccionado {selectd}")
        form_main()

    if selectd == "Registro de avances":
        st.write(f"Haz seleccionado {selectd}")

    if selectd == "Visualizaciones":
        st.write(f"Haz seleccionado {selectd}")
    
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
    
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')