import streamlit as st
from streamlit_option_menu import option_menu

def progress_record_main():
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
        
        st.title("Registro de datos")
        
        selectd = option_menu(
            menu_title=None,
            options=["Hoja de evolución", "Notas"],
            orientation="horizontal"
        )
        
        # Cuestionario
        if selectd == "Hoja de evolución":

            with st.form("Hoja de evolución", clear_on_submit=True):
                col1_sec1, col2_sec1 = st.columns(2)

                with col1_sec1:
                    weight = st.number_input('Peso', min_value=0.0, max_value=3.0, format="%0.2f")
                    IMC = st.number_input('Índice de masa corporal', min_value=0.0, max_value=3.0, format="%0.2f")
                
                with col2_sec1:
                    size = st.number_input('Talla', min_value=0.0, max_value=3.0, format="%0.2f")
                    body_fat = st.number_input('Porcentaje de grasa corporal', min_value=0.0, max_value=3.0, format="%0.2f")

                submitted = st.form_submit_button("Enviar")

        if selectd == "Notas":
            st.write("En construcción")
        