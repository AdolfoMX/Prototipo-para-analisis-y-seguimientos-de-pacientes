import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import time

st.set_page_config(
    page_title="SLSM app",
    page_icon=":heart:",
    initial_sidebar_state="auto"
)
    
# Autenticación del usuario
names = ["admin"]
usernames = ["admin"]
passwords = ["12345"]

hashed_password = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_password, "login SLSM", "auth", cookie_expiry_days=0)
name, authentication_status, username = authenticator.login("Login", "main")

# Verificación
if authentication_status:
    time.sleep(0.5)
    
    with st.sidebar:
        
        # Inicio de código
        st.markdown(
            """
            <style>
                [data-testid=stSidebar] [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-top: -28%;
                    margin-left: auto;
                    margin-right: auto%;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.image(".\\prototipo_2\\images\\image.png", width=180, use_column_width=False)
        selectd = option_menu(
            menu_title="Menú principal",
            options=
                [
                    "Inicio", 
                    "Pacientes", 
                    "Cuestionario SLSM", 
                    "Registro de avances", 
                    "Visualizaciones"
                ],
            icons= 
                [
                    "house", 
                    "people",
                    "file-medical",
                    "percent",
                    "bar-chart"
                ]
        )
        authenticator.logout('Logout', 'main')
    
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
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
    
elif authentication_status is None:
    st.warning('Please enter your username and password')