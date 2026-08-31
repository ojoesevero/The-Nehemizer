# 📜 Registro de Mudanças (Changelog)

Todas as alterações notáveis no projeto **The Nehemizer** serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.1.0] - 2026-08-31

### ✨ Adicionado
- **Arquitetura Modular (`src/`):** Divisão de responsabilidades em `config/`, `services/` e `utils/`.
- **Guia Inicial & Download de Template:** Tela amigável de boas-vindas com instruções e botão para baixar planilha de exemplo (`Template_Vendas_TheNehemizer_Exemplo.xlsx`).
- **Filtro Rápido de Preços Pendentes:** Toggle `🔍 Apenas preços pendentes` para facilitar o preenchimento rápido de itens sem preço de compra.
- **Gráficos Executivos:** Visualização gráfica de faturamento por cliente e distribuição de itens (Contrato BD vs Aba NORMAL).
- **Parser de PDF com Regex Flexível:** Suporte a múltiplos padrões de formatação monetária (com e sem `R$`, pontos e vírgulas) e identificação de clientes em páginas múltiplas.
- **Persistência de Sessão (`st.session_state`):** Garantia de retenção das edições manuais e do arquivo exportado durante a navegação.

### 🔄 Alterado
- **Refatoração do `app.py`:** Redução de complexidade, servindo como orquestrador principal e delegando regras aos módulos especializados.
- **Melhorias Visuais no README:** Estruturação semântica com HTML5, badges interativas e tabelas estilizadas com padrão Saavedra N3.

---

## [1.0.0] - 2026-08-30

### 🚀 Lançamento Inicial
- **Leitura Resiliente de Vendas:** Suporte a arquivos `.xlsx`, `.xls` e `.csv` com múltiplos encodings e descoberta dinâmica de linha de cabeçalho.
- **Parser de Contratos BD em PDF:** Extração automática de tabelas com `pdfplumber` e `@st.cache_data`.
- **Regra Suprema de Contingência:** Alocação de produtos com contrato BD para suas respectivas abas e direcionamento de itens sem contrato para a aba `NORMAL`.
- **Prévia Interativa:** Tabela editável com `st.data_editor` para preenchimento de preços faltantes.
- **Exportação Multi-Aba com XlsxWriter:** Geração de planilha com **Aba RESUMO** estilizada e abas analíticas por cliente com subtotais e totais gerais.
