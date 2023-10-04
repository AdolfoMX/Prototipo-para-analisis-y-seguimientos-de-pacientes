import streamlit as st
from streamlit_option_menu import option_menu

import datetime as dt

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
            options=["Formulario", "Hojas de evolución", "Notas del paciente"],
            orientation="horizontal"
        )
        
        # Cuestionario
        if selectd == "Formulario":

            with st.form("Hoja de evolución", clear_on_submit=True):
                current_date = dt.date.today()
                date_now = st.text_input(":blue[Fecha de registro]", value=current_date.strftime("%d/%m/%y"), disabled=True)
                
                col1_sec1, col2_sec1 = st.columns(2)
                
                with col1_sec1:
                    weight = st.number_input('Peso (kg)', min_value=0.0, max_value=200.0, format="%0.2f")
                    IMC = st.number_input('Índice de masa corporal (IMC)', min_value=0.0, max_value=40.0, format="%0.2f")
                    visceral_fat = st.number_input('Grasa visceral (%)', min_value=0.0, max_value=60.0, format="%0.2f")
                    muscle = st.number_input('Porcentaje de musculo (%)', min_value=0.0, max_value=45.0, format="%0.2f")
                    abdomen = st.number_input('Perimetro abdominal (cm)', min_value=0.0, max_value=120.0, format="%0.2f")
                    exercise = st.number_input('Minutos al día de ejercicio', min_value=1, max_value=720)
                    hours_sleep = st.number_input('Horas de sueño', min_value=1, max_value=12)
                
                with col2_sec1:
                    size = st.number_input('Talla (cm)', min_value=0, max_value=100)
                    body_fat = st.number_input('Porcentaje de grasa corporal (%)', min_value=0.0, max_value=40.0, format="%0.2f")
                    metabolic_age = st.number_input('Edad metabólica', min_value=1, max_value=100)
                    calories = st.number_input('Consumo de calorias (kcal)', min_value=1000, max_value=3000)
                    glucose = st.number_input('Glucosa en sangre (mg/dl)', min_value=1000, max_value=3000)
                    junk_food = st.selectbox('Apetito de comida chatarra', 
                                                       ('Mucha','Poca','Casi nada','Nada'))
                    sleep_quality = st.selectbox('Calidad de sueño', 
                                                       ('Bastante buena','Buena','Mala','Bastante mala'))
                notes = st.text_area('Notas de la sesión')

                submitted = st.form_submit_button("Enviar")

        if selectd == "Hojas de evolución":
            st.write("En construcción")
        

        if selectd == "Notas del paciente":
            st.write("En construcción")