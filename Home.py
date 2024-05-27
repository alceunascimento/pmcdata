import streamlit as st
import pandas as pd

# Configurar o layout do site
st.set_page_config(
    page_title="Mercado Imobiliário de Curitiba",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Página principal
st.title("Dados do Mercado Imobiliário de Curitiba")
st.header("",divider='red')
st.markdown(
        """
        Este projeto visa fornecer uma visão quantitativa sobre o mercado imobiliário de Curitiba.    
        Da base de dados da Prefeitura Municipal de Curitiba são obtidos dados sobre a produção de estoque imobiliário e sobre a comercialização dos imóveis.  
        A formação de estoque é observada através da emissão de alvarás de construção e de certificados de conclusão e vistoria de obra.  
        Já a comercialização é observada através dos dados de lançamentos de Imposto de Transmissão de Bens Imóveis.  
        """
)
