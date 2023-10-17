import streamlit as st
from streamlit_option_menu import option_menu

import mysql.connector
import datetime as dt
import re

def form(id_user):
    #Cuestionario
    with st.form("Hoja de evolución", clear_on_submit=True):
        current_date = dt.date.today()
        date_now = st.text_input(":blue[Fecha de registro]", value="DD/MM/YYYY", disabled=True)

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
        notes = st.text_area('Notas de la sesión', max_chars=200)

        submitted = st.form_submit_button("Enviar")

        if submitted:
            try:
                cnx = mysql.connector.connect(
                    user='root', 
                    password='12345',
                    host='127.0.0.1',
                    database='slsm_db'
                )

                cursor = cnx.cursor()
                
                sql = """
                INSERT INTO hojas_evolucion_medico (
                    id_usuario,
                    fecha_registro,
                    peso,
                    IMC,
                    grasa_viseral,
                    porcentaje_musculo,
                    abdomen,
                    ejercicio,
                    horas_sueno,
                    talla,
                    grasa_corporal,
                    edad_metabolica,
                    calorias,
                    glucosa,
                    comida_chatarra,
                    calidad_sueno,
                    notas
                ) 
                VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,
                        %s,	%s,	%s,	%s,	%s,	%s,	%s	                   
                )
                """
                
                val = (
                    id_user,
                    current_date,
                    weight,
                    IMC,
                    visceral_fat,
                    muscle,
                    abdomen,
                    exercise,
                    hours_sleep,
                    size,
                    body_fat,
                    metabolic_age,
                    calories,
                    glucose,
                    junk_food,
                    sleep_quality,
                    notes
                )
                
                cursor.execute(sql, val)
                cnx.commit()
                
                cursor.close()
                cnx.close()
            except:
                st.warning("Por favor asegurese de llenar todos los campos")


def check_users_db(full_name):
    cnx = mysql.connector.connect(
        user='root', 
        password='12345',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    
    sql = f"SELECT id_usuario, CONCAT(nombre, ' ', apellidos) AS nombre_completo FROM usuarios WHERE id_rol = 2 AND CONCAT(nombre, ' ', apellidos) LIKE '%{full_name}%'"
    cursor.execute(sql)

    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    
    return result
    
def evolution_sheets(id_user):
    # Colocar codigo aqui
    cnx = mysql.connector.connect(
        user='root', 
        password='12345',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    
    sql = f"SELECT * FROM hojas_evolucion_medico"
    cursor.execute(sql)

    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    
    #current_date.strftime("%d/%m/%y")
    date = st.date_input("Selecciona una fecha de búsqueda", min_value=dt.date(2023,1,1), format="DD/MM/YYYY")
    
    #st.write(result)
    #print(result[0][0])
    #print(type(date))
    #print(type(result[0][0]))
    #st.write(result)
    #st.write(date)
    #st.write(id_user)
    
    for i in range(len(result)):
        st.subheader(f":date: {i+1}. Fecha: :blue[{date}]", divider='green')
        
        with st.expander(f"Ver hoja {i+1}..."):
            col1_sec1, col2_sec1 = st.columns(2)

            with col1_sec1:
                st.text_input('Peso (kg)', value=result[i][3], disabled=True, key=f"{i+1}.1")
                st.text_input('Índice de masa corporal (IMC)', value=result[i][4], disabled=True, key=f"{i+1}.2")
                st.text_input('Grasa visceral (%)', value=result[i][5], disabled=True, key=f"{i+1}.3")
                st.text_input('Porcentaje de musculo (%)', value=result[i][6], disabled=True, key=f"{i+1}.4")
                st.text_input('Perimetro abdominal (cm)', value=result[i][7], disabled=True, key=f"{i+1}.5")
                st.text_input('Minutos al día de ejercicio', value=result[i][8], disabled=True, key=f"{i+1}.6")
                st.text_input('Horas de sueño', value=result[i][9], disabled=True, key=f"{i}.7")

            with col2_sec1:
                st.text_input('Talla (cm)', value=result[i][9], disabled=True, key=f"{i+1}.8")
                st.text_input('Porcentaje de grasa corporal (%)', value=result[i][10], disabled=True, key=f"{i+1}.9")
                st.text_input('Edad metabólica', value=result[i][11], disabled=True, key=f"{i+1}.10")
                st.text_input('Consumo de calorias (kcal)', value=result[i][12], disabled=True, key=f"{i+1}.11")
                st.text_input('Glucosa en sangre (mg/dl)', value=result[i][13], disabled=True, key=f"{i+1}.12")
                st.text_input('Apetito de comida chatarra', value=result[i][14], disabled=True, key=f"{i+1}.13")
                st.text_input('Calidad de sueño', value=result[i][15], disabled=True, key=f"{i+1}.14")
                
            st.text_area('Notas de la sesión', value=result[i][16], disabled=True, key=f"{i+1}.15")
    
    
    """
    if date == result[5][0]:
        st.write("Fecha exacta")
        print("Fecha exacta")
    """
    
    col1_genel, col2_genel = st.columns(2)
    """
    with col1_genel:
        weight = st.number_input('Peso (kg)', value= result[0][0], disabled=True)
        IMC = st.number_input('Índice de masa corporal (IMC)', value= result[0][2], disabled=True)
        visceral_fat = st.number_input('Grasa visceral (%)', value= result[0][4], disabled=True)
        muscle = st.number_input('Porcentaje de musculo (%)', value= result[0][6], disabled=True)
        abdomen = st.number_input('Perimetro abdominal (cm)', value= result[0][8], disabled=True)
        exercise = st.number_input('Minutos al día de ejercicio', value= result[0][10], disabled=True)
        hours_sleep = st.number_input('Horas de sueño', value= result[0][12], disabled=True)

    with col2_genel:
        size = st.number_input('Talla (cm)', value= result[0][1], disabled=True)
        body_fat = st.number_input('Porcentaje de grasa corporal (%)', value= result[0][3], disabled=True)
        metabolic_age = st.number_input('Edad metabólica', value= result[0][5], disabled=True)
        calories = st.number_input('Consumo de calorias (kcal)', value= result[0][7], disabled=True)
        glucose = st.number_input('Glucosa en sangre (mg/dl)', value= result[0][9], disabled=True)
        junk_food = st.selectbox('Apetito de comida chatarra', value= result[0][11], disabled=True)
        sleep_quality = st.selectbox('Calidad de sueño', value= result[0][13], disabled=True)
        
    notes = st.text_area('Notas de la sesión', value= result[0][14], disabled=True)
    """

def patient_notes():
    # Colocar codigo aqui
    
    pass

def progress_record_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
                
                data
            </style>
            """, unsafe_allow_html=True
        )
        
        if 'list_users' not in st.session_state:
            st.session_state['list_users'] = [""]
        
        st.title("Registro de datos")

        col1, col2 = st.columns(2)        
        with col1:
            search_pacient = st.text_input("Buscador", value="")
            submitted = st.button("Enviar")

        if submitted:
            search_pacient = " ".join(search_pacient.upper().split())
            
            if search_pacient != "":
                results_db = check_users_db(" ".join(search_pacient.upper().split()))
                
                if not results_db:
                    st.session_state['list_users'] = [""]
                    st.warning("El paciente no está registrado")
                else:
                    st.session_state['list_users'] = ["ID " + str(data[0]) + ". "+ data[1] for data in results_db]
        
        with col2:
            selectd_user = st.selectbox("Paciente(s)", st.session_state['list_users'])
            st.info(f"\\[ Selección ]: {selectd_user}")
            
        st.subheader("", divider="orange")
        
        if selectd_user != "":
            id_user = re.search(r"\d+", selectd_user)
            id_user = int(id_user.group())
            
            selectd = option_menu(
                menu_title=None,
                options=["Formulario", "Hojas de progreso", "Notas del paciente"],
                orientation="horizontal"
            )
            
            if selectd == "Formulario":
                form(id_user)
            
            if selectd == "Hojas de progreso":
                evolution_sheets(id_user)
                
            
            if selectd == "Notas del paciente":
                st.write("En construcción")

"""
                if submitted:
                    cnx = mysql.connector.connect(
                        user='root', 
                        password='12345',
                        host='127.0.0.1',
                        database='slsm_db'
                    )

                    cursor = cnx.cursor()
                    
                    sql = "
                    INSERT INTO hojas_evolucion_medico (
                        id_usuario,
                        fecha_registro,
                        peso,
                        IMC,
                        grasa_viseral,
                        porcentaje_musculo,
                        abdomen,
                        ejercicio,
                        horas_sueno,
                        talla,
                        grasa_corporal,
                        edad_metabolica,
                        calorias,
                        glucosa,
                        comida_chatarra,
                        calidad_sueno,
                        notas
                    ) 
                    VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,
                            %s,	%s,	%s,	%s,	%s,	%s,	%s	                   
                    )
                    "
                
                    
                    val = (
                        st.session_state['id_user'],
                        date_now,
                        weight,
                        IMC,
                        visceral_fat,
                        muscle,
                        abdomen,
                        exercise,
                        hours_sleep,
                        size,
                        body_fat,
                        metabolic_age,
                        calories,
                        glucose,
                        junk_food,
                        sleep_quality,
                        notes
                    )
                    
                    cursor.execute(sql, val)
                    cnx.commit()
                    
                    cursor.close()
                    cnx.close()



date_now,

weight,
IMC,
visceral_fat,
muscle,
abdomen,
exercise,
hours_sleep,

size,
body_fat,
metabolic_age,
calories,
glucose,
junk_food,
sleep_quality,
notes
"""