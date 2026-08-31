"""Componentes visuais, cards KPI, gráficos e guias interativos da interface."""

import streamlit as st
import pandas as pd
from src.config.settings import APP_TITLE, APP_SUBTITLE, APP_VERSION, APP_ICON, CUSTOM_CSS, PRIMARY_COLOR, DARK_NEUTRAL
from src.services.table_service import gerar_template_exemplo_vendas


def render_header():
    """Renderiza a barra de título e injeção do CSS corporativo Saavedra."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.markdown(
        f'<div class="main-title">{APP_ICON} {APP_TITLE} <span class="badge-version">v{APP_VERSION}</span></div>',
        unsafe_allow_html=True
    )
    st.markdown(f'<p class="sub-title">{APP_SUBTITLE}</p>', unsafe_allow_html=True)


def render_guia_inicial():
    """Renderiza painel explicativo e botão de template quando nenhum arquivo de vendas estiver anexado."""
    st.info("Para iniciar a equalização e consolidação, faça o upload do relatório de vendas nos campos acima.")
    
    col_g1, col_g2, col_g3 = st.columns(3)
    with col_g1:
        st.markdown("""
        #### 1. Relatório de Vendas
        * Arquivos `.xlsx`, `.xls` ou `.csv`
        * Identificação heurística de cabeçalho
        * Mapeamento de `REFPROD`, `VLRTOTAL`, `RAZAOSOCIAL`
        """)
    with col_g2:
        st.markdown("""
        #### 2. Contratos BD (PDF)
        * Propostas comerciais Becton Dickinson
        * Extração de preços unitários tabelados
        * Suporte a múltiplos PDFs em lote
        """)
    with col_g3:
        st.markdown("""
        #### 3. Tabela Preço Normal
        * Tabela padrão de custos (Excel/CSV)
        * Preenchimento para itens fora de contrato BD
        * Destinação automática para aba `NORMAL`
        """)
        
    st.divider()
    
    st.markdown("#### 📥 Planilha Modelo para Testes")
    template_bytes = gerar_template_exemplo_vendas()
    st.download_button(
        label="📄 Baixar Planilha Modelo (.xlsx)",
        data=template_bytes,
        file_name="Template_Vendas_TheNehemizer_Exemplo.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        help="Baixe uma planilha estruturada para testar as regras de negócio do sistema."
    )


def render_kpis_e_graficos(df: pd.DataFrame):
    """Exibe painel executivo de KPIs e gráficos de distribuição de receita e contratos."""
    total_linhas = len(df)
    total_bd = df['TEM_PRECO_BD'].sum()
    total_normal = total_linhas - total_bd
    vlr_total_venda = df['VLRTOTAL'].sum()
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Total de Linhas", f"{total_linhas:,}")
    with kpi2:
        pct_bd = (total_bd / total_linhas * 100) if total_linhas > 0 else 0
        st.metric("Itens com Contrato BD", f"{total_bd:,}", delta=f"{pct_bd:.1f}%")
    with kpi3:
        pct_norm = (total_normal / total_linhas * 100) if total_linhas > 0 else 0
        st.metric("Itens na Aba NORMAL", f"{total_normal:,}", delta=f"-{pct_norm:.1f}%", delta_color="inverse")
    with kpi4:
        st.metric("Total Vendas", f"R$ {vlr_total_venda:,.2f}")

    # Gráficos de Apoio com paleta oficial Saavedra
    with st.expander("📊 Análise de Distribuição e Cobertura", expanded=False):
        col_c1, col_c2 = st.columns(2)
        
        with col_c1:
            st.markdown("**Faturamento por Grupo de Cliente (R$)**")
            chart_data = df.groupby('GRUPO_CLIENTE')['VLRTOTAL'].sum().reset_index()
            chart_data = chart_data.sort_values(by='VLRTOTAL', ascending=False).set_index('GRUPO_CLIENTE')
            st.bar_chart(chart_data, color=PRIMARY_COLOR)
            
        with col_c2:
            st.markdown("**Proporção de Itens (Contrato BD vs NORMAL)**")
            status_data = pd.DataFrame({
                'Categoria': ['Contrato BD', 'Aba NORMAL'],
                'Qtd Itens': [int(total_bd), int(total_normal)]
            }).set_index('Categoria')
            st.bar_chart(status_data, color=DARK_NEUTRAL)
