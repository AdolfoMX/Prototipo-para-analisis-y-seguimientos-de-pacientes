import streamlit as st

def visualizations_patient_main():
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
        
        st.title("Gráficas de progreso")