# KEEP Engenharia - Sistema Executivo de Custos v1

Este repositório contém:
- um protótipo de app em Streamlit para gestão financeira, custos, orçamento, rentabilidade e controle de obras;
- um gerador de arquivo Excel .xlsx com a estrutura proposta para a KEEP Engenharia;
- dados fictícios para demonstração e testes iniciais.

## Objetivo

Transformar a gestão da empresa em um sistema executivo de custos, orçamento, rentabilidade e controle financeiro, alinhado ao futuro módulo do aplicativo de gestão de obras.

## Estrutura do projeto

- `app.py` — aplicativo principal em Streamlit
- `workbook_builder.py` — gerador do arquivo Excel
- `requirements.txt` — dependências do projeto
- `KEEP_Sistema_Executivo_Custos_v1.xlsx` — gerado pelo script (será criado ao executar o projeto)

## Como executar

1. Crie um ambiente virtual
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o app
   ```bash
   streamlit run app.py
   ```

4. Gere o Excel
   - no app, clique no botão de download;
   - ou execute:
   ```bash
   python workbook_builder.py
   ```

## Conteúdo do protótipo

- Dashboard executivo
- Cadastro de pessoas, veículos e equipamentos
- Cadastro de clientes e obras/serviços
- Orçamento por obra
- Lançamentos de receitas e custos
- Despesas administrativas
- Formação de preço
- DRE gerencial
- Fluxo de caixa
- Indicadores e alertas
- Estrutura pensada para futuro sistema e integração com app de obra

## Observação importante sobre tributação

Os percentuais tributários são configuráveis e precisam ser validados com a contabilidade da empresa. A planilha não substitui assessoria contábil.
