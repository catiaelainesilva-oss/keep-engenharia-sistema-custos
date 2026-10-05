import streamlit as st
import pandas as pd
from io import BytesIO
from workbook_builder import generate_workbook

st.set_page_config(page_title="KEEP Engenharia - Sistema Executivo", layout="wide")

st.title("KEEP ENGENHARIA")
st.caption("Sistema Executivo de Custos, Orçamento, Rentabilidade e Controle Financeiro")

with st.sidebar:
    st.header("Configurações")
    empresa = st.text_input("Nome da empresa", "KEEP Engenharia")
    regime = st.text_input("Regime tributário", "Simples Nacional")
    margem_minima = st.number_input("Margem mínima %", 0.0, 100.0, 15.0, 0.5)
    margem_recomendada = st.number_input("Margem recomendada %", 0.0, 100.0, 20.0, 0.5)
    horas_produtivas = st.number_input("Horas produtivas padrão/mês", 1, 500, 160, 1)
    custo_indireto = st.number_input("Custos indiretos %", 0.0, 100.0, 15.0, 0.5)
    contingencia = st.number_input("Contingência %", 0.0, 100.0, 8.0, 0.5)
    meta_faturamento = st.number_input("Meta de faturamento mensal", 0.0, 100000000.0, 250000.0, 1000.0)
    meta_lucro = st.number_input("Meta de lucro mensal", 0.0, 100000000.0, 35000.0, 1000.0)

st.subheader("Resumo executivo")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Faturamento", "R$ 420.000")
col2.metric("Custos Diretos", "R$ 258.000")
col3.metric("Lucro Bruto", "R$ 162.000")
col4.metric("Despesas", "R$ 74.000")
col5.metric("Lucro Líquido", "R$ 88.000")

st.markdown("---")

# Dados ilustrativos
kpis = {
    "Receita Bruta": 420000,
    "Custos Diretos": 258000,
    "Lucro Bruto": 162000,
    "Despesas Indiretas": 74000,
    "Lucro Líquido": 88000,
    "Margem Líquida": 20.95,
}

base_df = pd.DataFrame(
    {
        "Categoria": [
            "Mão de obra",
            "Materiais",
            "Terceiros",
            "Combustível",
            "Equipamentos",
            "Despesas administrativas",
            "Impostos",
            "Outros"
        ],
        "Valor": [120000, 60000, 30000, 14000, 18000, 42000, 15000, 12000],
        "Participação %": [28.6, 14.3, 7.1, 3.3, 4.3, 10.0, 3.6, 2.9],
    }
)

st.write("Onde o dinheiro está indo")
st.dataframe(base_df, use_container_width=True)

st.markdown("---")

# Gráficos em Streamlit
chart_df = pd.DataFrame(
    {
        "Mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Receita": [300000, 340000, 390000, 420000, 460000, 500000],
        "Custo": [180000, 210000, 240000, 258000, 278000, 295000],
        "Lucro": [120000, 130000, 150000, 162000, 182000, 205000],
    }
)

st.line_chart(chart_df.set_index("Mes"))

# Exportação do arquivo Excel
st.markdown("---")
st.subheader("Gerar arquivo Excel")

if st.button("Gerar Excel v1"):
    workbook_bytes = generate_workbook()
    st.download_button(
        label="Baixar KEEP_Sistema_Executivo_Custos_v1.xlsx",
        data=workbook_bytes,
        file_name="KEEP_Sistema_Executivo_Custos_v1.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

st.markdown("---")

st.subheader("Resumo de rentabilidade por serviço")
service_df = pd.DataFrame(
    {
        "Serviço": ["Obra", "Reforma", "Projeto", "Laudo", "Vistoria", "Consultoria", "Fiscalização", "Gerenciamento"],
        "Faturamento": [250000, 120000, 80000, 35000, 30000, 60000, 50000, 70000],
        "Custo": [160000, 78000, 42000, 18000, 17000, 32000, 26000, 37000],
        "Lucro": [90000, 42000, 38000, 17000, 13000, 28000, 24000, 33000],
        "Margem %": [36.0, 35.0, 47.5, 48.6, 43.3, 46.7, 48.0, 47.1],
    }
)

st.dataframe(service_df, use_container_width=True)
