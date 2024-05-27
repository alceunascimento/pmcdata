import streamlit as st


st.set_page_config(page_title="Sobre", layout="wide")
st.header("Sobre",divider='red')
st.markdown(
"""
### 1. Descrição do Projeto

O projeto tem como objetivo a criação de um website que disponibilize dados do mercado imobiliário de Curitiba. Este website será desenvolvido utilizando a biblioteca Streamlit e apresentará informações provenientes de três conjuntos de dados distintos: transações imobiliárias (ITBI), alvarás de construção emitidos e certificados de conclusão e vistoria de obra. A estrutura do site será composta por uma página principal que explicará o projeto, além de três páginas específicas que exibirão os dados detalhados de cada categoria mencionada. A iniciativa visa aumentar a transparência imobiliária municipal, proporcionando um acesso mais amplo e estruturado às informações sobre o mercado imobiliário de Curitiba.  
Este projeto está sendo desenvolvido por Alceu Eilert Nascimento, no âmbito do Programa de Pós-Gradução em Estatística e Informática e de Pós-Graduação em Economia da Universidade Federal do Paraná.
Contado do autor: alceu@ufpr.br 

### 2. Justificativa do Projeto

A falta de transparência no mercado imobiliário brasileiro é um problema significativo que afeta a precificação de ativos, o tempo de venda de imóveis e o acesso ao crédito. Atualmente, não existem dados abertos e consolidados sobre transações imobiliárias, o que obriga compradores, vendedores e locatários a se basearem em informações de anúncios, corretores e conhecidos. Esse cenário contribui para uma má precificação dos imóveis e um longo tempo para a venda, comparado a outros países. 

Informações transacionais são disponibilizadas em cartórios, porém de forma descentralizada e a um custo elevado. A disponibilidade de dados estruturados em larga escala é fundamental para estudos de mercado e investimentos mais informados. Dados hiper locais são essenciais para uma precificação precisa, considerando variáveis como endereço, posição solar e estado de conservação dos imóveis.

Com a disponibilização desses dados, é possível criar modelos preditivos que melhoram as estimativas de valor dos imóveis. Isso não apenas beneficia compradores e vendedores, mas também bancos e instituições financeiras ao facilitar a emissão de crédito imobiliário com maior precisão e rapidez, reduzindo custos operacionais.

A transparência imobiliária também tende a reduzir a distorção nos preços médios dos imóveis, especialmente beneficiando famílias de menor renda. Diversos estudos e exemplos internacionais demonstram os benefícios da divulgação de dados transacionais, como a redução na assimetria de informação entre vendedores e compradores e a consequente estabilização dos preços de mercado.

A implementação deste projeto por parte das prefeituras, utilizando bases de dados do ITBI, contribuirá para a redução da assimetria de informações no mercado imobiliário, aumentando a transparência e promovendo um desenvolvimento econômico mais equilibrado. Além disso, atenderá às disposições constitucionais de acesso à informação, conforme previsto no inciso XXXIII do art. 5º da Constituição Federal, promovendo uma maior segurança jurídica para todos os envolvidos no processo.

### Referências:
- https://www.us.jll.com/en/trends-and-insights/research/global-real-estate-transparency-index
- https://www.miamidade.gov/pa/online_tools.asp
- https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
- https://institutodegovernoaberto.com.br/publicacoes/
- https://dados.pbh.gov.br/dataset/relatorio-itbi
- https://www.prefeitura.sp.gov.br/cidade/secretarias/fazenda/acesso_a_informacao/index.php?p=31501
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2357112
- https://www.sciencedirect.com/science/article/abs/pii/S0094119019300464
"""
)