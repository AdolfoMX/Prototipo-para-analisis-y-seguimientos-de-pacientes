import streamlit as st
import mysql.connector

def general_data_view(id_user):
    cnx = mysql.connector.connect(
        user='root', 
        password='12345',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    sql = f"SELECT nombre, apellidos, correo FROM usuarios WHERE id_usuario = '{id_user}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    sql2 = "SELECT fecha_nacimiento, numero_telefono, genero FROM historiales_medicos"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    if not result2:
        result2 = [("", "", "")]
        
    col1_genel, col2_genel = st.columns(2)
    
    with col1_genel:
        name = st.text_input("Nombre", value=result[0][0], disabled=True)
        email = st.text_input("Correo electrónico", value=result[0][2], disabled=True)
        date = st.text_input("Fecha de nacimiento", value=result2[0][0], disabled=True)
        
    with col2_genel:
        last_name = st.text_input("Apellidos", value=result[0][1], disabled=True)
        number_phone = st.text_input("Número de teléfono", value=result2[0][1], disabled=True)
        genre = st.text_input("Sexo", value=result2[0][2], disabled=True)

def information_patient_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
                
                div[data-testid="stExpander"] div[role="button"] p {
                    font-size: 1.1rem;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.title("Perfil")
        
        with st.expander("**Datos generales**"):
            general_data_view(st.session_state['id_user'])
         
        with st.expander("**Historial médico**"):
            st.write("En construcción")