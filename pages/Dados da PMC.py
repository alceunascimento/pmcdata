import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dataframes
df_transacoes = pd.read_csv('data/transacoes.csv')
df_alvaras = pd.read_csv('data/alvaras.csv')
df_cvcso = pd.read_csv('data/cvcos.csv')



# Configurar o layout do site
st.set_page_config(
    page_title="Mercado Imobiliário de Curitiba",
    layout="wide",
    initial_sidebar_state="expanded",
)





# Página de transações
# Certifique-se de que a coluna 'data' está no formato datetime
df_transacoes['data'] = pd.to_datetime(df_transacoes['data'], format='%Y%m%d')
# Filtrar os dados para os últimos 12 meses
df_transacoes_last_12_months = df_transacoes[df_transacoes['data'] >= (pd.Timestamp.today() - pd.DateOffset(months=12))]
# Agrupar por mês e calcular o valor acumulado de 'area'
df_transacoes_last_12_months['month'] = df_transacoes_last_12_months['data'].dt.to_period('M')
df_transacoes_valor_acumulada = df_transacoes_last_12_months.groupby('month')['valor'].sum().cumsum().reset_index()
df_transacoes_valor_acumulada['month'] = df_transacoes_valor_acumulada['month'].dt.to_timestamp()

def transacoes_page():
    st.title("Transações Imobiliárias")
    st.header("", divider='red')
    
    # Criar duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Análise Estatística")
        st.write(df_transacoes.describe())
    
    with col2:
        st.markdown("### Valores Acumulada nos Últimos 12 Meses")
        fig, ax = plt.subplots()
        ax.plot(df_transacoes_valor_acumulada['month'], df_transacoes_valor_acumulada['valor'], marker='o')
        ax.set_title("R$ Acumulados por Mês")
        ax.set_xlabel("Mês")
        ax.set_ylabel("R$")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    st.markdown("### Base de Dados de Lançamentos de Imposto de Transmissão de Bens Imóveis (ITBI)")
    st.dataframe(df_transacoes)




# Página de alvarás de construção
# Certifique-se de que a coluna 'data' está no formato datetime
df_alvaras['data_1a_emissao'] = pd.to_datetime(df_alvaras['data_1a_emissao'], format='%Y%m%d')
# Filtrar os dados para os últimos 12 meses
df_alvaras_last_12_months = df_alvaras[df_alvaras['data_1a_emissao'] >= (pd.Timestamp.today() - pd.DateOffset(months=12))]

# Agrupar por mês e calcular o valor acumulado de 'area'
df_alvaras_last_12_months['month'] = df_alvaras_last_12_months['data_1a_emissao'].dt.to_period('M')
df_alvaras_area_acumulada = df_alvaras_last_12_months.groupby('month')['area_total'].sum().cumsum().reset_index()
df_alvaras_area_acumulada['month'] = df_alvaras_area_acumulada['month'].dt.to_timestamp()

def alvaras_page():
    st.title("Alvarás de Construção")
    st.header("", divider='red')
    
    # Criar duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Análise Estatística")
        st.write(df_alvaras.describe())
    
    with col2:
        st.markdown("### Área Construída Acumulada nos Últimos 12 Meses")
        fig, ax = plt.subplots()
        ax.plot(df_alvaras_area_acumulada['month'], df_alvaras_area_acumulada['area_total'], marker='o')
        ax.set_title("Área (m²) Acumulada por Mês")
        ax.set_xlabel("Mês")
        ax.set_ylabel("Área Acumulada (m²)")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    st.markdown("### Base de Dados de Lançamentos de Imposto de Transmissão de Bens Imóveis (ITBI)")
    st.dataframe(df_alvaras)

# Página de certificados de conclusão e vistoria de obra
def cvcso_page():
    st.title("Certificados de Conclusão e Vistoria de Obra")
    st.header("",divider='red')
    st.markdown("### Base de Dados de Certificados de Conclusão e Vistoria de Obra emitidos")
    st.dataframe(df_cvcso)
    st.markdown("### Análise Estatística")
    st.write(df_cvcso.describe())

# Mapeamento das páginas
page_names_to_funcs = {
    "Transações Imobiliárias": transacoes_page,
    "Alvarás de Construção": alvaras_page,
    "Certificados de Conclusão e Vistoria de Obra": cvcso_page,
}

# Sidebar para navegação
selected_page = st.sidebar.selectbox("Selecione", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
