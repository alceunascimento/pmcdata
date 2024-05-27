import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dataframes
df_despejos = pd.read_csv('data/despejos.csv')
df_vicios = pd.read_csv('data/vicios.csv')



# Configurar o layout do site
st.set_page_config(
    page_title="Mercado Imobiliário de Curitiba",
    layout="wide",
    initial_sidebar_state="expanded",
)





# Página de despejos
def despejos_page():
    st.title("Ações de Despejo")
    st.header("", divider='red')
    
    # Criar duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Análise Estatística")
        st.write(df_despejos.describe())
    

    
    st.markdown("### Base de Dados de Lançamentos de Imposto de Transmissão de Bens Imóveis (ITBI)")
    st.dataframe(df_despejos)




# Página de vicios construtivos

def vicios_page():
    st.title("Vícios Construtivos")
    st.header("", divider='red')
    
    # Criar duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Análise Estatística")
        st.write(df_vicios.describe())
    
    
    st.markdown("### Base de Dados de Lançamentos de Imposto de Transmissão de Bens Imóveis (ITBI)")
    st.dataframe(df_vicios)



# Mapeamento das páginas
page_names_to_funcs = {
    "Despejos": despejos_page,
    "Vícios Construtivos": vicios_page,
}

# Sidebar para navegação
selected_page = st.sidebar.selectbox("Selecione", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
