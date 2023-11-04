import requests
import streamlit as st
import numpy as np

st.set_page_config(page_title='Bem-vindos, batch 1365!!')

st.markdown('# Olhem só quantas funções show')

if st.button('Clique em mim, se quiser'):
    st.image('raw_data/nosso_professor.jpeg')


query = st.text_input('Assunto do GIF')
url = 'https://api.giphy.com/v1/gifs/search'
params = {
    'api_key': st.secrets.api_keys.api_key,
    'q': query,
    'limit': 10
}

response = requests.get(url, params=params).json()

while not query:
    st.stop()

gif_url = response['data'][np.random.randint(0, 10)]['embed_url']

st.components.v1.iframe(gif_url, width=480, height=240)

st.write(st.secrets.new_session.avada)
