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
        
        st.title("Perfil")

        #name = st.write(st.session_state['name'])
        st.write("¡ Bienvenido, ", st.session_state.name,"!")

        #if st.experimental_user.name:
            
        #    name = get_name_from_db(st.experimental_user.name)
        
        