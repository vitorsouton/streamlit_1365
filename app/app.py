import streamlit as st
import numpy as np
import pandas as pd

st.markdown(
    '''
    # Hello world
    ### Sub-header
    ---
    * Essa
    * E uma
    * Lista
    ---
    $\dfrac{x}{y}$
    '''
)

with st.echo():
    st.checkbox('Eu sou uma checkbox')


df = pd.read_csv('raw_data/spotify_songs.csv')

line_counter = st.slider('Quantas linhas mostrar:', 1, 10, 3)

head_df = df.head(line_counter)

head_df
