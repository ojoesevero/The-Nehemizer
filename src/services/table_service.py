"""Serviço de leitura, higienização e geração de templates de tabelas (Excel / CSV)."""

import io
import pandas as pd


def ler_arquivo_tabela(file) -> pd.DataFrame:
    """
    Lê arquivos Excel (.xlsx, .xls) ou CSV (.csv) com tolerância a múltiplos encodings,
    delimitadores e detecção automática de linha de cabeçalho.
    """
    filename = str(file.name).lower()
    if filename.endswith('.csv'):
        # Tenta diferentes separadores e encodings comuns em sistemas legados
        for enc in ['utf-8', 'latin1', 'cp1252']:
            for sep in [',', ';', '\t']:
                try:
                    file.seek(0)
                    df_temp = pd.read_csv(file, nrows=25, header=None, encoding=enc, sep=sep)
                    linha_cabecalho = 0
                    for i, row in df_temp.iterrows():
                        linha_texto = "".join(str(val).upper() for val in row.values)
                        if any(k in linha_texto for k in ["RAZAOSOCIAL", "CONVENIO", "REF", "PRODUTO", "VALOR", "QUANT"]):
                            linha_cabecalho = i
                            break
                    file.seek(0)
                    return pd.read_csv(file, header=linha_cabecalho, encoding=enc, sep=sep)
                except Exception:
                    continue
        file.seek(0)
        return pd.read_csv(file)
    else:
        df_temp = pd.read_excel(file, nrows=25, header=None)
        linha_cabecalho = 0
        for i, row in df_temp.iterrows():
            linha_texto = "".join(str(val).upper() for val in row.values)
            if any(k in linha_texto for k in ["RAZAOSOCIAL", "CONVENIO", "REF", "PRODUTO", "VALOR"]):
                linha_cabecalho = i
                break
        return pd.read_excel(file, header=linha_cabecalho)


def gerar_template_exemplo_vendas() -> bytes:
    """Gera uma planilha de exemplo em Excel para o usuário baixar e testar."""
    dados_exemplo = [
        {
            "CONTRATOCLIENTE": "450128261",
            "CNPJPARCEIRO": "87.096.616/0001-52",
            "UF": "RS",
            "CODCLIUSO": "1001",
            "RAZAOSOCIAL": "UNIMED PORTO ALEGRE COOP MEDICA",
            "CNPJPARCUSO": "87.096.616/0001-52",
            "CONVENIO": "CONV-01",
            "REFPROD": "300600",
            "DESCRICAO": "CATETER INTRAVENOSO BD INSYTE AUTOGUARD",
            "QTDCOM": 500,
            "VLRTOTAL": 2500.00
        },
        {
            "CONTRATOCLIENTE": "450155842",
            "CNPJPARCEIRO": "88.630.413/0001-00",
            "UF": "RS",
            "CODCLIUSO": "1002",
            "RAZAOSOCIAL": "UNIAO BRASILEIRA DE EDUCACAO E ASSISTENCIA PUC",
            "CNPJPARCUSO": "88.630.413/0001-00",
            "CONVENIO": "CONV-02",
            "REFPROD": "381423",
            "DESCRICAO": "SERINGA DESCARTAVEL BD PLASTIPAK 20ML",
            "QTDCOM": 1000,
            "VLRTOTAL": 1800.00
        },
        {
            "CONTRATOCLIENTE": "",
            "CNPJPARCEIRO": "00.000.000/0001-99",
            "UF": "RS",
            "CODCLIUSO": "1003",
            "RAZAOSOCIAL": "CLINICA MEDICA EXEMPLO LTDA",
            "CNPJPARCUSO": "00.000.000/0001-99",
            "CONVENIO": "CONV-03",
            "REFPROD": "999999",
            "DESCRICAO": "LUVA DE PROCEDIMENTO NITRILICA",
            "QTDCOM": 200,
            "VLRTOTAL": 600.00
        }
    ]
    df_exemplo = pd.DataFrame(dados_exemplo)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_exemplo.to_excel(writer, sheet_name='VENDAS_EXEMPLO', index=False)
    return output.getvalue()
