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
            options=["Hoja de evolución"],
            orientation="horizontal"
        )
        
        # Cuestionario
        if selectd == "Hoja de evolución":
            st.write("En construcción...")