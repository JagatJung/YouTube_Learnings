from audioop import reverse
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.title("NHA Player stats Explorer")

st.markdown('''
This is app that performs simple webscraping of NBA player stats data!
* **Python Libraries** base64, pandas, streamlit
* **Data Source** [Basketball-reference.com]

''')

st.sidebar.header("User inpput Features")

selected_year=st.sidebar.selectbox('Year', list(reversed(range(1990,2021))))


@st.cache
def load_data(year):
    url="https://www.basketball-reference.com/players/a"
    html=pd.read_html(url,header=0)
    df=html[0]
    df = df.drop(['Birth Date'], axis=1)
    df = df.dropna()
    #raw=raw.fillna(0)
    #playerstats=raw
    return df

player_stats=load_data(selected_year)


sorted_Colleges=sorted(player_stats.Colleges.unique())
selected_team=st.sidebar.multiselect("Colleges",sorted_Colleges,sorted_Colleges)

unique_pos=sorted(player_stats.Pos.unique())
select_pos=st.sidebar.multiselect("position", unique_pos,unique_pos)

show_team=player_stats[(player_stats.Colleges.isin(selected_team)) & (player_stats.Pos.isin(select_pos))]

st.header("Statics of the players from selected data")
st.dataframe(show_team)

def file_download(df):
    csv=df.to_csv(index=False)
    b64=base64.b64encode(csv.encode()).decode()
    href=f' <a href= "data:file/csv ; base64, {b64}" download="playerstats.csv"> Download CSV File </a>'
    return href

st.markdown(file_download(show_team), unsafe_allow_html=True)

if st.button('HeatMap'):
    st.header("Intercorrelatio Matrix HeatMap")
    show_team.to_csv('output.csv', index=False)
    df=pd.read_csv('output.csv')

    corr=df.corr()
    mask=np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    with sns.axes_style("white"):

        fig, ax = plt. subplots(figsize=(7,10))
        ax=sns.heatmap(corr, mask=mask, vmax=1, square = True)

    st.pyplot(fig)
