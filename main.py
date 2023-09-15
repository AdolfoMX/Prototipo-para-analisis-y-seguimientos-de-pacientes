import streamlit as st
from streamlit_option_menu import option_menu

import pages_app.authenticator_user as stauth
from pages_app.interfaz_specialist.specialist_view import specialist_view_main
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
        
    if "rol_logout" not in st.session_state:
        st.session_state["rol_logout"] = authenticator
        
    # Interfaz del especialista
    specialist_view_main()
    
    # Interfaz de usuario
    # Pendiente...
    
elif st.session_state['authentication_status'] is False:
    st.error('Usuario/contraseña es incorrecto')
    
elif st.session_state['authentication_status'] is None:
    st.warning('Por favor ingrese su usuario y contraseña')