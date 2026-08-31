"""Configurações centrais, mapeamentos de contratos e constantes visuais da Saavedra."""

APP_TITLE = "The Nehemizer - Portal Financeiro Saavedra"
APP_SUBTITLE = "O peso justo e a organização perfeita para os seus contratos financeiros. (Inspirado em Provérbios 11:1 e Neemias)"
APP_VERSION = "1.1.0"
APP_ICON = "🎸"

# Paleta Corporativa Saavedra
PRIMARY_COLOR = "#F37021"      # Laranja Saavedra
SECONDARY_COLOR = "#333333"    # Grafite Escuro
BG_CARD_COLOR = "#F8FAFC"      # Fundo suave
TEXT_MUTED = "#475569"         # Texto secundário

# Mapeamento Oficial de Contratos BD
CONTRATOS_MAPPING = {
    'UNIMED': '450128261',
    'PUC': '450155842',
    'H DIVINA': '450146829',
    'HCPA': '450139832',
    'SMS POA': '450120243',
    'EBSERH': '450098658',
    'HCAA': '450137626',
    'GHC': '450166419',
    'CONCEICAO': '450166419'
}

# CSS Customizado Corporativo
CUSTOM_CSS = f"""
    <style>
        .main-title {{
            color: {PRIMARY_COLOR};
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 0px;
        }}
        .sub-title {{
            color: {TEXT_MUTED};
            font-size: 1.05rem;
            font-style: italic;
            margin-bottom: 1.5rem;
        }}
        .metric-card {{
            background-color: {BG_CARD_COLOR};
            border-left: 5px solid {PRIMARY_COLOR};
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .badge-version {{
            background-color: {PRIMARY_COLOR};
            color: white;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: bold;
            display: inline-block;
            margin-left: 10px;
            vertical-align: middle;
        }}
        .stButton>button {{
            border-radius: 6px;
            font-weight: bold;
        }}
    </style>
"""
