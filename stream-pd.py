import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import time

selected_page = option_menu(
        menu_title=None, 
        options = ['Ankieta', 'Staty'], 
        icons= ['pencil', 'bar-chart'],
        menu_icon = 'cast',
        default_index=0, 
        orientation='horizontal'
    )

if selected_page == 'Ankieta':
    firstname = st.text_input("Wprowadź swoje imię:", placeholder= "Wpisz tutaj...")
    surname = st.text_input("Wprowadź swoje nazwisko:", placeholder= "Wpisz tutaj...")
    if st.button("ZAPISZ"):
        result = firstname.title()
        result2 = surname.title()
        if firstname.title() == '' or surname.title() == '':
            st.error("Sprawdź czy wypełniłeś/aś pola!")
        else:
            st.success("Poprawnie wprowadzono dane do kwestionariusza: " + result + " " + result2)

elif selected_page == 'Staty':
    data = st.file_uploader("Wczytaj swoje dane...", type=['csv'])
    if data is not None:
        with st.spinner('Poczekaj...'):
            time.sleep(5)
        df = pd.read_csv(data)
        st.dataframe(df.head(10))
        which_visual = st.selectbox("Wybierz typ wykresu:", ("Histogram", "Słupkowy"))
        if which_visual == 'Histogram':
            selected_col = st.selectbox("Wybierz kolumnę:", df.columns)
            fig = px.histogram(df, x = df[selected_col].values)
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        elif which_visual == 'Słupkowy':
            x_selected_col = st.selectbox("Wybierz kolumnę x:", df.columns)
            y_selected_col = st.selectbox("Wybierz kolumnę y:", df.columns)
            st.bar_chart(data=df, x=x_selected_col, y=y_selected_col)