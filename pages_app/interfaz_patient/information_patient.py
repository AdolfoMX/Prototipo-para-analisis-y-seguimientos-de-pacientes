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
            st.write("En construcción")
         
        with st.expander("**Historial médico**"):
            st.write("En construcción")