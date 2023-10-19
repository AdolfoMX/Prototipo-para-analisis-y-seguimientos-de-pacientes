import streamlit as st
from streamlit_option_menu import option_menu

import mysql.connector
import datetime as dt

def progress_record_patient_main():
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
        
        st.title("Registro de avances")
        
        selectd = option_menu(
            menu_title=None,
            options=["Hoja de evolución"],
            orientation="horizontal"
        )
        
        # Cuestionario
        if selectd == "Hoja de evolución":
            
            with st.form("Historial médico", clear_on_submit=True):
                current_date = dt.date.today()
                date_now = st.text_input(":blue[Fecha de registro]", value=current_date.strftime("%d/%m/%y"), disabled=True)
                
                # Sección 1 de preguntas
                st.subheader("Sección 1. Salud física")
                col1_sec1, col2_sec1 = st.columns(2)

                with col1_sec1:
                    quest1_sec1 = st.slider("Indique del 1 al 10 cómo se siente físicamente tras la última sesión: ", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec1)

                with col2_sec1:
                    notes1_sec1 = st.text_area("¿Cómo se sintió físicamente?", max_chars=200)
                
                notes2_sec1 = st.text_area("¿Notó mejoras?", max_chars=200)

                st.divider()

                # Sección 2 de preguntas
                st.subheader("Sección 2. Enfermedades crónicas")
                col1_sec2, col2_sec2 = st.columns(2)
                
                
                with col1_sec2:
                    quest1_sec2 = st.slider("Indique del 1 al 10 cuánto considera que ha progresado en su salud", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec2)
                
                with col2_sec2:
                    notes1_sec2 = st.text_area("¿Cómo se sintió respecto a su salud?", max_chars=200)
                
                notes2_sec2 = st.text_area("¿Notó mejoras? ", max_chars=200)
                
                st.divider()

                # Sección 3 de preguntas
                st.subheader("Sección 3. Salud mental")
                col1_sec3, col2_sec3 = st.columns(2)
                
                with col1_sec3:
                    quest1_sec3 = st.slider("Indique del 1 al 10 cuánto considera que ha progresado en su salud mental", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec3)
                
                with col2_sec3:
                    notes1_sec3 = st.text_area("¿Cómo se sintió respecto a su salud mental?", max_chars=200)
                
                notes2_sec3 = st.text_area("¿Notó mejoras?  ", max_chars=200)
                
                st.divider()

                # Sección 4 de preguntas
                st.subheader("Sección 4. Conciliación del sueño")
                col1_sec4, col2_sec4 = st.columns(2)
                
                
                with col1_sec4:
                    quest1_sec4 = st.slider("Indique del 1 al 10 cuánto considera que ha progresado en su conciliación del sueño", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec4)
                
                with col2_sec4:
                    notes1_sec4 = st.text_area("¿Cómo se sintió respecto a su sueño?", max_chars=200)
                
                notes2_sec4 = st.text_area("¿Notó mejoras?   ", max_chars=200)
                
                st.divider()

                # Sección 5 de preguntas
                st.subheader("Sección 5. Alimentación")
                col1_sec5, col2_sec5 = st.columns(2)
                
                with col1_sec5:
                    quest1_sec5 = st.slider("Indique del 1 al 10 cuánto considera que ha progresado en su alimentación", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec4)
                
                with col2_sec5:
                    notes1_sec5 = st.text_area("¿Cómo se sintió respecto a su alimentación?", max_chars=200)
                
                notes2_sec5 = st.text_area("¿Notó mejoras?     ", max_chars=200)
                
                st.divider()

                # Sección 6 de preguntas
                st.subheader("Sección 6. Adicciones y/o consumos")
                col1_sec6, col2_sec6 = st.columns(2)
                
                
                with col1_sec6:
                    quest1_sec6 = st.slider("Indique del 1 al 10 cuánto considera que ha progresado en las adicciones y/o consumo (tabaco y/o alcohol)", 0,10,5)
                    #st.write("Puntaje: ", quest1_sec4)
                
                with col2_sec6:
                    notes1_sec6 = st.text_area("¿Cómo se sintió respecto al consumo y/o adicciones?", max_chars=200)
                
                notes2_sec6 = st.text_area("¿Notó mejoras?      ", max_chars=200)
                
                st.divider()

                #Sección 7 de preguntas
                st.subheader("Sección 7. Avances generales")
                
                quest1_sec7 = st.text_area("En general, ¿Cómo se sintió tras esta última sesión?", max_chars = 200)

                st.divider()
                    
                submitted = st.form_submit_button("Enviar")
                
                if  submitted:
                    try:
                        cnx = mysql.connector.connect(
                            user='root', 
                            password='12345',
                            host='127.0.0.1',
                            database='slsm_db'
                        )

                        cursor = cnx.cursor()
                        
                        sql = """INSERT INTO avances_usuarios (
                            id_usuario,
                            fecha_registro,
                            pregunta1_sec1,
                            notas1_sec1,
                            notas2_sec1,
                            pregunta1_sec2,
                            notas1_sec2,
                            notas2_sec2,
                            pregunta1_sec3,
                            notas1_sec3,
                            notas2_sec3,
                            pregunta1_sec4,
                            notas1_sec4,
                            notas2_sec4,
                            pregunta1_sec5,
                            notas1_sec5,
                            notas2_sec5,
                            pregunta1_sec6,
                            notas1_sec6,
                            notas2_sec6,
                            pregunta1_sec7
                        ) 
                        VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,
                                %s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s                
                        )
                        """

                        val = (
                            st.session_state['id_user'],
                            current_date,
                            quest1_sec1,
                            notes1_sec1,
                            notes2_sec1,
                            quest1_sec2,
                            notes1_sec2,
                            notes2_sec2,
                            quest1_sec3,
                            notes1_sec3,
                            notes2_sec3,
                            quest1_sec4,
                            notes1_sec4,
                            notes2_sec4,
                            quest1_sec5,
                            notes1_sec5,
                            notes2_sec5,
                            quest1_sec6,
                            notes1_sec6,
                            notes2_sec6,
                            quest1_sec7
                        )
                        
                        cursor.execute(sql, val)
                        cnx.commit()
                        
                        cursor.close()
                        cnx.close()
                        st.success('La información ha sido registrada!', icon="✅")
                    except:
                        st.warning("Por favor asegurese de llenar todos los campos", icon="⚠️")


"""
date_now,
quest1_sec1,
notes1_sec1,
notes2_sec1,
quest1_sec2,
notes1_sec2,
notes2_sec2,
quest1_sec3,
notes1_sec3,
notes2_sec3,
quest1_sec4,
notes1_sec4,
notes2_sec4,
quest1_sec5,
notes1_sec5,
notes2_sec5,
quest1_sec6,
notes1_sec6,
notes2_sec6,
quest1_sec7
"""