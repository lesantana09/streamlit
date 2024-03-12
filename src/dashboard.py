import requests
import streamlit as st
import pandas as pd


def formata_numero(valor, prefixo=''):
    for unidade in ['', 'mil']:
        if valor < 1000: 
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'

st.title("DashBoard de Vendas :shopping_trolley:")

url  = "https://labdados.com/produtos"
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

colunas1, coluna2 = st.columns(2)

with colunas1:
    st.metric("Receita", formata_numero(dados["Preço"].sum(), 'R$'))

with coluna2:
    st.metric("Quantidade de Vendas", formata_numero(dados.shape[0]))

st.dataframe(dados)

