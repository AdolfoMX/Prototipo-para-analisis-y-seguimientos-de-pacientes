import streamlit as st

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
            col1_genel, col2_genel = st.columns(2)
                
            with col1_genel:
                name = st.text_input("Nombre")
                email = st.text_input("Correo electrónico")
                date = st.text_input("Fecha de nacimiento")
                    
            with col2_genel:
                last_name = st.text_input("Apellidos")
                number_phone = st.text_input("Número de teléfono")
                genre = st.text_input("Sexo")
         
        with st.expander("**Historial médico**"):
            st.write("En construcción")