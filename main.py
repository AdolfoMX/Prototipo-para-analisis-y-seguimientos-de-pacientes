import streamlit as st
from streamlit_option_menu import option_menu

import pages_app.authenticator_user as stauth
from pages_app.interfaz_specialist.specialist_view import specialist_view_main
from pages_app.interfaz_patient.patient_view import patient_view_main

import time

st.set_page_config(
    page_title="SLSM app",
    page_icon=":hospital:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Autenticación de usuarios
names = ["admin", "adolfo"]
usernames = ["admin", "adolfo"]
passwords = ["12345", "12345"]
hashed_password = ["$2b$12$nflzQj3nySx8F44R3TGpeO0DoaQraODD5MQrEa.By/Sf9n2Vc9wLK", "$2b$12$QBv5LBJOb0gg2lpyxewznuJd6CUdXWCx5njqhyevr0p20iQRD5YJG"]

authenticator = stauth.Authenticate(names, usernames, hashed_password, "SLSM app", "auth", cookie_expiry_days=30)

#time.sleep(0.2)

# Inicio de sesión
name, authentication_status, username = authenticator.login("Inicio de sesión", "main")

# Verificación
if st.session_state['authentication_status']:  
    
    time.sleep(0.08)
        
    if "rol_logout" not in st.session_state:
        st.session_state["rol_logout"] = authenticator
    
    if name == "admin":
        # Interfaz del especialista
        specialist_view_main()
    
    if name == "adolfo":
        # Interfaz de paciente
        patient_view_main()
    
elif st.session_state['authentication_status'] is False:
    st.error('Usuario/contraseña es incorrecto')
    
    # Registro de usuario
    authenticator.register_user()
    
elif st.session_state['authentication_status'] is None:
    st.warning('Por favor ingrese su usuario y contraseña')
    
    # Registro de usuario
    authenticator.register_user()