from pathlib import Path
from utilidades import leitura_de_dados

import streamlit as st
import pandas as pd

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

st.sidebar.markdown('## Seleção de Tabelas')
tabela_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:', ['Vendas','Produtos','Filiais'])

def mostrar_tabela_produtos():
    st.dataframe(df_produtos)

def mostrar_tabela_filiais():
    st.dataframe(df_filiais)

def mostrar_tabela_vendas():
    st.sidebar.divider()
    st.sidebar.markdown('### Filtrar tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas de tabela:',
                                                            list(df_vendas.columns),
                                                            list(df_vendas.columns))
    col1, col2 = st.sidebar.columns(2)
    filtro_selecionado = col1.selectbox('Filtrar coluna', list(df_vendas.columns))
    valores_unicos_coluna = list(df_vendas[filtro_selecionado].unique())
    valor_filtro = col2.selectbox('Valor do filtro', valores_unicos_coluna)

    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[filtro_selecionado] == valor_filtro, colunas_selecionadas],height=800)
    elif limpar:
        st.dataframe(df_vendas[colunas_selecionadas],height=800)
    else:
        st.dataframe(df_vendas[colunas_selecionadas],height=800)

if tabela_selecionada == 'Produtos':
    mostrar_tabela_produtos()
elif tabela_selecionada == 'Filiais':
    mostrar_tabela_filiais()
elif tabela_selecionada == 'Vendas':
    mostrar_tabela_vendas()


