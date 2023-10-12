import streamlit as st
from streamlit_option_menu import option_menu

import mysql.connector
import datetime as dt

def form_main():
    with st.container():
        
        # Inicio de código
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
            options=["Historial médico"],
            orientation="horizontal"
        )
        
        # Cuestionario
        if selectd == "Historial médico":
            with st.form("Historial médico", clear_on_submit=True):
        
                # Sección 1 de preguntas
                st.subheader("Sección 1. Datos generales del paciente")
                col1_sec1, col2_sec1 = st.columns(2)
                
                with col1_sec1:
                    date = st.date_input("Fecha de nacimiento",min_value=dt.date(1960,1,1),format="DD/MM/YYYY")
                    height = st.number_input('Altura', min_value=0.0, max_value=3.0, format="%0.2f")
                    
                with col2_sec1:
                    number_phone = st.text_input("Número de teléfono")
                    genre = st.radio("Sexo", index=2, options=["Masculino", "Femenino", "Otro"], horizontal=True)
                    
                weight = st.number_input('Peso', min_value=0.0, max_value=200.0, step=0.1, format="%0.1f")
                
                st.divider()
                
                # Sección 2 de preguntas
                st.subheader("Sección 2. Salud Física")
                col1_sec2, col2_sec2 = st.columns(2)

                with col1_sec2:
                    quest1_sec2 = st.radio("¿Haces alguna actividad física?", options=["Si", "No"], horizontal=False)
                    quest3_sec2 = st.radio("¿Tienes sobrepeso?", options=["Si", "No"], horizontal=False)
                    quest5_sec2 = st.number_input("Cuántos años con sobrepeso lleva", min_value=0, max_value=50, step=1)
                    quest7_sec2 = st.text_area("¿Qué complicaciones ha tenido (sobrepeso)?", max_chars=200)
                    quest9_sec2 = st.number_input("Cuántos días a la semana hace ejercicio moderado", min_value=0, max_value=7, step=1)
                    quest11_sec2 = st.text_area("Cuando no hace ejercicio, ¿qué se lo impide?", max_chars=200)
                    
                with col2_sec2:
                    quest2_sec2 = st.number_input("¿Cuántos días a la semana realizas actividad física?", min_value=0, max_value=7, step=1)
                    quest4_sec2 = st.number_input("¿Cuántos kilos de sobrepeso tiene?", min_value=0.0, max_value=200.0, step=0.1, format="%0.1f")
                    quest6_sec2 = st.radio("¿Ha tenido alguna complicación por el sobrepeso?", options=["Si", "No"], horizontal=False)
                    quest8_sec2 = st.number_input("Cuántos minutos hace ejercicio moderado", min_value=0, max_value=1440, step=1)
                    quest10_sec2 = st.text_area("¿Qué le motiva hacer ejercicio?", max_chars=200)
                    quest12_sec2 = st.text_area("¿El ejercicio le causa problemas de salud?", max_chars=200)
                    
                quest13_sec2 = st.text_area("¿Sabe cuándo su cuerpo está tenso o estresado?", max_chars=200)
                
                st.divider()
                
                # Sección 3 de preguntas
                st.subheader("Sección 3. Enfermedades crónicas")
                col1_sec3, col2_sec3 = st.columns(2)

                with col1_sec3:
                    quest1_sec3 = st.radio("¿Tiene hipertensión?", options=["Si", "No"], horizontal=False)
                    quest3_sec3 = st.radio("¿Ha tenido alguna complicación por la hipertensión?", options=["Si", "No"], horizontal=False)
                    quest5_sec3 = st.radio("¿Tiene diabetes?", options=["Si", "No"], horizontal=False)
                    quest7_sec3 = st.radio("¿Ha tenido alguna complicación por la diabetes?", options=["Si", "No"], horizontal=False)
                    quest9_sec3 = st.radio("¿Tiene alguna enfermedad cardíaca?", options=["Si", "No"], horizontal=False)
                    quest11_sec3 = st.radio("¿Ha tenido alguna complicación por la enfermedad cardíaca?", options=["Si", "No"], horizontal=False)
                    quest13_sec3 = st.radio("¿Tiene alguna enfermedad cerebral?", options=["Si", "No"], horizontal=False)
                    quest15_sec3 = st.radio("¿Ha tenido alguna complicación por la enfermedad cerebral?", options=["Si", "No"], horizontal=False)

                with col2_sec3:
                    quest2_sec3 = st.number_input("¿Cuántos años lleva padeciendo de hipertensión?", min_value=0, max_value=100, step=1)
                    quest4_sec3 = st.text_area("¿Qué complicaciones ha tenido por la hipertensión?", max_chars=200)
                    quest6_sec3 = st.number_input("¿Cuántos años lleva padeciendo de diabetes?", min_value=0, max_value=100, step=1)
                    quest8_sec3 = st.text_area("¿Qué complicaciones ha tenido por la diabetes?", max_chars=200)
                    quest10_sec3 = st.number_input("¿Cuántos años lleva padeciendo la enfermedad cardíaca?", min_value=0, max_value=100, step=1)
                    quest12_sec3 = st.text_area("¿Qué complicaciones ha tenido por la enfermedad cardíaca?", max_chars=200)
                    quest14_sec3 = st.number_input("¿Cuántos años lleva padeciendo la enfermedad cerebral?", min_value=0, max_value=100, step=1)
                    quest16_sec3 = st.text_area("¿Qué complicaciones ha tenido por la enfermedad cerebral?", max_chars=200)
                
                quest17_sec3 = st.text_area("¿Qué otras enfermedades crónicas ha tenido?", max_chars=200)
                    
                st.divider()
                
                # Sección 4 de preguntas
                st.subheader("Sección 4. Salud mental")
                col1_sec4, col2_sec4 = st.columns(2)
                
                with col1_sec4:
                    quest1_sec4 = st.radio("¿Siente que no tiene control en cosas importantes de su vida?", options=["Si", "No"], horizontal=False)
                    quest3_sec4 = st.radio("¿Siente que su vida no va como quisiera?", options=["Si", "No"], horizontal=False)
                    quest5_sec4 = st.text_area("¿Qué tan frecuente siente que su vida no tiene próposito o sentido?", max_chars=200)
                    quest7_sec4 = st.radio("¿Sus pensamientos o emociones afectan su salud física?", options=["Si", "No"], horizontal=False)
                    quest9_sec4 = st.radio("¿Se ha sentido abatido, deprimido o sin esperanza?", options=["Si", "No"], horizontal=False)
                    quest11_sec4 = st.radio("¿Siente que es un fracaso para si mismo o su familia?", options=["Si", "No"], horizontal=False)
                    quest13_sec4 = st.radio("¿Fácilmente se irrita o molesta?", options=["Si", "No"], horizontal=False)
                    quest15_sec4 = st.radio("¿Cuándo sufre estrés extremo siente que puede aprender de eso?", options=["Si", "No"], horizontal=False)
                    quest17_sec4 = st.radio("¿Cumple sus propias metas?", options=["Si", "No"], horizontal=False)
                    quest19_sec4 = st.radio("¿Hay personas que le apoyan en caso necesario?", options=["Si", "No"], horizontal=False)
                    quest21_sec4 = st.radio("¿Está satisfecho con su Sistema de Creencias?", options=["Si", "No"], horizontal=False)

                with col2_sec4:
                    quest2_sec4 = st.radio("¿Se siente incapaz de manejar sus problemas personales?", options=["Si", "No"], horizontal=False)
                    quest4_sec4 = st.radio("¿Siente que no puede librarse de lo que le molesta?", options=["Si", "No"], horizontal=False)
                    quest6_sec4 = st.radio("¿En su vida ha pensado seriamente suicidarse?", options=["Si", "No"], horizontal=False)
                    quest8_sec4 = st.radio("¿En las ultimas 3 semanas ha sentido poca alegría o placer de las cosas?", options=["Si", "No"], horizontal=False)
                    quest10_sec4 = st.radio("¿Ha perdido el apetito o come demasiado a causa de su estado emocional?", options=["Si", "No"], horizontal=False)
                    quest12_sec4 = st.radio("¿Tiene problemas para concentrarse?", options=["Si", "No"], horizontal=False)
                    quest14_sec4 = st.text_area("Si tu respuesta anterior es sí, ¿Qué realizas para controlarlo?", max_chars=200)
                    quest16_sec4 = st.radio("¿Le es fácil saber lo que es prioritario?", options=["Si", "No"], horizontal=False)
                    quest18_sec4 = st.radio("¿Vive una vida con propósito o significado?", options=["Si", "No"], horizontal=False)
                    quest20_sec4 = st.radio("¿Tiene su propia fortaleza interna?", options=["Si", "No"], horizontal=False)
                    quest22_sec4 = st.text_area("¿Cómo califica su vida social?", max_chars=200)

                st.divider()
                
                # Sección 5 de preguntas
                st.subheader("Sección 5. Conciliación del sueño")
                col1_sec5, col2_sec5 = st.columns(2)
                
                with col1_sec5:
                    quest1_sec5 = st.radio("¿Tiene algún problema de salud que le impide dormir?", options=["Si", "No"], horizontal=False)
                    quest3_sec5 = st.radio("¿Se despierta en la noche y no puede volver a dormir?", options=["Si", "No"], horizontal=False)
                    quest5_sec5 = st.radio("¿Su trabajo le obliga a estar despierto de noche?", options=["Si", "No"], horizontal=False)
                    quest7_sec5 = st.radio("¿Cuantás horas al día duerme habitualmente?", options=["4 o menos", "4 a 6 horas", "6 a 8 horas", "8 o más"], horizontal=False)
                    
                with col2_sec5:
                    quest2_sec5 = st.text_area("Si su respuesta fue afirmativa, ¿qué problema de salud tiene?", max_chars=200)
                    quest4_sec5 = st.radio("¿Sus problemas le quitan el sueño o le hacen dormir mucho?", options=["Me quitan el sueño", "Duermo más de lo normal", "Ninguna de las anteriores"], horizontal=False)
                    quest6_sec5 = st.radio("¿Necesita hacer siesta?", options=["Si", "No"], horizontal=False)
                    
                st.divider()
                
                # Sección 6 de preguntas
                st.subheader("Sección 6. Alimentación")
                col1_sec6, col2_sec6 = st.columns(2)
                
                with col1_sec6:
                    quest1_sec6 = st.number_input("¿Cuántas veces ingiere comida “chatarra” a la semana?", min_value=0, max_value=100, step=1)
                    quest3_sec6 = st.radio("¿Ha intentado alguna dieta o plan de nutrición?", options=["Si", "No"], horizontal=False)
                    quest5_sec6 = st.radio("¿Cena abundante?", options=["Si", "No"], horizontal=False)
                    
                with col2_sec6:
                    quest2_sec6 = st.multiselect("¿Cuál es su tipo de alimentación?", ["Omnívoro", "Vegetariano", "Vegano", "Otro"])
                    quest4_sec6 = st.radio("¿Respeta sus “horas de comida” a lo largo del día?", options=["Si", "No"], horizontal=False)
                    quest6_sec6 = st.radio("¿Sentirse estresado le motiva a tomar alimentos?", options=["Si", "No"], horizontal=False)

                st.divider()
                
                # Sección 7 de preguntas
                st.subheader("Sección 7. Adicciones y/o consumos")
                col1_sec7, col2_sec7 = st.columns(2)

                with col1_sec7:
                    quest1_sec7 = st.radio("A lo largo de su vida ¿ha fumado más de 100 cigarrillos (5 paquetes)?", options=["Si", "No"], horizontal=False)
                    quest3_sec7 = st.text_area("En el ultimo año, ¿con qué frecuencia ha consumido bebidas alcohólicas?", max_chars=200)

                with col2_sec7:
                    quest2_sec7 = st.radio("¿Ha usado fármacos para bajar de peso?", options=["Si", "No"], horizontal=False)
                    quest4_sec7 = st.radio("¿Se ha sentido culpable por su forma de beber o le critican por ello?", options=["Si", "No"], horizontal=False)

                st.divider()
                
                # Sección extra
                st.subheader("Sección extra")
                col1_ext, col2_ext = st.columns(2)

                with col1_ext:
                    quest1_ext = st.radio("¿Su salud actual le limita hacer su vida normal?", options=["Sí", "No"], horizontal=False)
                    quest3_ext = st.radio("¿Cuánta confianza tiene de recuperar su buena salud?", options=["Sí", "No"], horizontal=False)
                    quest5_ext = st.radio("¿Cuáles serían las 5 causas por las que podría fallar de la pregunta anterior?", options=["Sí", "No"], horizontal=False)

                with col2_ext:
                    quest2_ext = st.text_area("De la pregunta anterior describe el porque", max_chars=200)
                    quest4_ext = st.text_area("¿Qué fortalezas personales o familiares usará en su propósito de salud?", max_chars=200)
                    quest6_ext = st.multiselect("Seleccione sus 3 propósitos más importantes", ["Mejor nutrición", "Peso ideal", "Dormir mejor", "Dejar algún vicio", "Salud emocional", "Mejor vida social"], max_selections=3)

                submitted = st.form_submit_button("Enviar")
                
                # codigo para almacenar los datos en la base de datos
                if submitted:
                    try:
                        cnx = mysql.connector.connect(
                            user='root', 
                            password='12345',
                            host='127.0.0.1',
                            database='slsm_db'
                        )

                        cursor = cnx.cursor()
                        sql_check = f"SELECT * FROM historiales_medicos WHERE id_usuario = '{st.session_state['id_user']}'"
                        cursor.execute(sql_check)
                        result_check = cursor.fetchall()
                        
                        if not result_check:
                            sql = """
                            INSERT INTO historiales_medicos (
                                id_usuario,
                                fecha_nacimiento,
                                altura,
                                numero_telefono,
                                genero,
                                peso,
                                pregunta1_sec2,
                                pregunta2_sec2,
                                pregunta3_sec2,
                                pregunta4_sec2,
                                pregunta5_sec2,
                                pregunta6_sec2,
                                pregunta7_sec2,
                                pregunta8_sec2,
                                pregunta9_sec2,
                                pregunta10_sec2,
                                pregunta11_sec2,
                                pregunta12_sec2,
                                pregunta13_sec2,
                                pregunta1_sec3,
                                pregunta2_sec3,
                                pregunta3_sec3,
                                pregunta4_sec3,
                                pregunta5_sec3,
                                pregunta6_sec3,
                                pregunta7_sec3,
                                pregunta8_sec3,
                                pregunta9_sec3,
                                pregunta10_sec3,
                                pregunta11_sec3,
                                pregunta12_sec3,
                                pregunta13_sec3,
                                pregunta14_sec3,
                                pregunta15_sec3,
                                pregunta16_sec3,
                                pregunta17_sec3,
                                pregunta1_sec4,
                                pregunta2_sec4,
                                pregunta3_sec4,
                                pregunta4_sec4,
                                pregunta5_sec4,
                                pregunta6_sec4,
                                pregunta7_sec4,
                                pregunta8_sec4,
                                pregunta9_sec4,
                                pregunta10_sec4,
                                pregunta11_sec4,
                                pregunta12_sec4,
                                pregunta13_sec4,
                                pregunta14_sec4,
                                pregunta15_sec4,
                                pregunta16_sec4,
                                pregunta17_sec4,
                                pregunta18_sec4,
                                pregunta19_sec4,
                                pregunta20_sec4,
                                pregunta21_sec4,
                                pregunta22_sec4,
                                pregunta1_sec5,
                                pregunta2_sec5,
                                pregunta3_sec5,
                                pregunta4_sec5,
                                pregunta5_sec5,
                                pregunta6_sec5,
                                pregunta7_sec5,
                                pregunta1_sec6,
                                pregunta2_sec6,
                                pregunta3_sec6,
                                pregunta4_sec6,
                                pregunta5_sec6,
                                pregunta6_sec6,
                                pregunta1_sec7,
                                pregunt2_sec7,
                                pregunta3_sec7,
                                pregunta4_sec7,
                                pregunta1_ext,
                                pregunta2_ext,
                                pregunta3_ext,
                                pregunta4_ext,
                                pregunta5_ext,
                                pregunta6_ext
                            ) 
                            VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	
                                    %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s, %s                     
                            )
                            """
                            
                            val = (
                                st.session_state['id_user'],
                                date,
                                height,
                                number_phone,
                                genre,
                                weight,
                                quest1_sec2, 
                                quest2_sec2, 
                                quest3_sec2, 
                                quest4_sec2, 
                                quest5_sec2, 
                                quest6_sec2, 
                                quest7_sec2, 
                                quest8_sec2, 
                                quest9_sec2, 
                                quest10_sec2, 
                                quest11_sec2, 
                                quest12_sec2, 
                                quest13_sec2,
                                quest1_sec3,
                                quest2_sec3, 
                                quest3_sec3, 
                                quest4_sec3, 
                                quest5_sec3, 
                                quest6_sec3, 
                                quest7_sec3, 
                                quest8_sec3, 
                                quest9_sec3, 
                                quest10_sec3, 
                                quest11_sec3, 
                                quest12_sec3, 
                                quest13_sec3, 
                                quest14_sec3, 
                                quest15_sec3, 
                                quest16_sec3, 
                                quest17_sec3, 
                                quest1_sec4,
                                quest2_sec4, 
                                quest3_sec4, 
                                quest4_sec4, 
                                quest5_sec4, 
                                quest6_sec4, 
                                quest7_sec4, 
                                quest8_sec4, 
                                quest9_sec4, 
                                quest10_sec4, 
                                quest11_sec4, 
                                quest12_sec4, 
                                quest13_sec4, 
                                quest14_sec4, 
                                quest15_sec4, 
                                quest16_sec4, 
                                quest17_sec4, 
                                quest18_sec4, 
                                quest19_sec4, 
                                quest20_sec4, 
                                quest21_sec4, 
                                quest22_sec4, 
                                quest1_sec5,
                                quest2_sec5, 
                                quest3_sec5, 
                                quest4_sec5,
                                quest5_sec5,
                                quest6_sec5, 
                                quest7_sec5, 
                                quest1_sec6, 
                                ", ".join(quest2_sec6),
                                quest3_sec6, 
                                quest4_sec6, 
                                quest5_sec6, 
                                quest6_sec6, 
                                quest1_sec7,
                                quest2_sec7, 
                                quest3_sec7, 
                                quest4_sec7, 
                                quest1_ext,
                                quest2_ext, 
                                quest3_ext, 
                                quest4_ext, 
                                quest5_ext, 
                                ", ".join(quest6_ext)
                            )
                            
                            cursor.execute(sql, val)
                            cnx.commit()
                            
                            cursor.close()
                            cnx.close()
                        else:
                            cursor.close()
                            cnx.close()
                            st.warning("Hay datos existentes sobre este usuario")
                    except:
                        st.warning("Por favor asegurese de llenar todos los campos")
                        
"""
# Sección 1 de preguntas
date = [DATE]
height = [FLOAT]
number_phone = [VARCHAR lim 20]
genre = [VARCHAR lim 2]
weight = [FLOAT]
                
                
# Sección 2 de preguntas
quest1_sec2 = [VARCHAR  lim 2]
quest2_sec2 = [INT]
quest3_sec2 = [VARCHAR lim 2]
quest4_sec2 = [FLOAT]
quest5_sec2 = [INT]
quest6_sec2 = [VARCHAR lim 2]
quest7_sec2 = [VARCHAR lim 200]
quest8_sec2 = [INT]
quest9_sec2 = [INT]
quest10_sec2 = [VARCHAR lim 200]
quest11_sec2 = [VARCHAR lim 200]
quest12_sec2 = [VARCHAR lim 200]
quest13_sec2 = [VARCHAR lim 200]


# Sección 3 de preguntas
quest1_sec3 = [VARCHAR lim 2]
quest2_sec3 = [INT]
quest3_sec3 = [VARCHAR lim 2]
quest4_sec3 = [VARCHAR lim 200]
quest5_sec3 = [VARCHAR lim 2]
quest6_sec3 = [INT]
quest7_sec3 = [VARCHAR lim 2]
quest8_sec3 = [VARCHAR lim 200]
quest9_sec3 = [VARCHAR lim 2]
quest10_sec3 = [INT]
quest11_sec3 = [VARCHAR lim 2]
quest12_sec3 = [VARCHAR lim 200]
quest13_sec3 = [VARCHAR lim 2]
quest14_sec3 = [INT]
quest15_sec3 = [VARCHAR lim 2]
quest16_sec3 = [VARCHAR lim 200]
quest17_sec3 = [VARCHAR lim 200]


# Sección 4 de preguntas
quest1_sec4 = [VARCHAR lim 2]
quest2_sec4 = [VARCHAR lim 2]
quest3_sec4 = [VARCHAR lim 2]
quest4_sec4 = [VARCHAR lim 2]
quest5_sec4 = [VARCHAR lim 200]
quest6_sec4 = [VARCHAR lim 2]
quest7_sec4 = [VARCHAR lim 2]
quest8_sec4 = [VARCHAR lim 2]
quest9_sec4 = [VARCHAR lim 2]
quest10_sec4 = [VARCHAR lim 2]
quest11_sec4 = [VARCHAR lim 2]
quest12_sec4 = [VARCHAR lim 2]
quest13_sec4 = [VARCHAR lim 2]
quest14_sec4 = [VARCHAR lim 200]
quest15_sec4 = [VARCHAR lim 2]
quest16_sec4 = [VARCHAR lim 2]
quest17_sec4 = [VARCHAR lim 2]
quest18_sec4 = [VARCHAR lim 2]
quest19_sec4 = [VARCHAR lim 2]
quest20_sec4 = [VARCHAR lim 2]
quest21_sec4 = [VARCHAR lim 2]
quest22_sec4 = [VARCHAR lim 200]


# Sección 5 de preguntas
quest1_sec5 = [VARCHAR lim 2]
quest2_sec5 = [VARCHAR lim 200]
quest3_sec5 = [VARCHAR lim 2]
quest4_sec5 = [VARCHAR lim 40]
quest5_sec5 = [VARCHAR lim 2]
quest6_sec5 = [VARCHAR lim 2]
quest7_sec5 = [VARCHAR lim 30]


# Sección 6 de preguntas
quest1_sec6 = [INT]
quest2_sec6 = [VARCHAR lim 15]
quest3_sec6 = [VARCHAR lim 2]
quest4_sec6 = [VARCHAR lim 2]
quest5_sec6 = [VARCHAR lim 2]
quest6_sec6 = [VARCHAR lim 2]


# Sección 7 de preguntas
quest1_sec7 = [VARCHAR lim 2]
quest2_sec7 = [VARCHAR lim 2]
quest3_sec7 = [VARCHAR lim 200]
quest4_sec7 = [VARCHAR lim 2]


# Sección extra
quest1_ext = [VARCHAR lim 2]
quest2_ext = [VARCHAR lim 200]
quest3_ext = [VARCHAR lim 2]
quest4_ext = [VARCHAR lim 200]
quest5_ext = [VARCHAR lim 2]
quest6_ext = [VARCHAR lim 22]
"""