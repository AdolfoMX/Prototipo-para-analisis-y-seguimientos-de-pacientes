import streamlit as st

def home_patient():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
            """, unsafe_allow_html=True
        )
        
        st.title("Inicio")
        st.divider()

        st.write("¡ Hola, ", st.session_state.name,"!")
        st.write("En SLSM creemos que el estilo de vida influye más que cualquier medicamento en nuestra salud. Pensamos que para mejorar no siempre es necesario recurrir a los medicamentos, sino que queremos brintarte la alternativa de progresar a través de un espacio donde podrás encontrar recursos y apoyo para aborar tu salud de manera equilibrada y prospera.")
        st.write("Adelantate, explora y mejora. Estamos emocionados de tenerte con nosotros mientras trabajamos en conjunto para una vida más saludable, fuerte y feliz")
        st.write("¡Bienvenido, ", st.session_state.name, "al programa Salud Latina Sin Medicina! Tu salud, tu bienestar.")

        with st.container():
            st.write("---")
            info_column, image_column = st.columns(2)
            with info_column:
                st.subheader("Mensaje de prueba")
                st.write("")

        st.button("Mi salud", type="primary")
        