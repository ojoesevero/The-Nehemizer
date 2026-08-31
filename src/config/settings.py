"""Configurações centrais, mapeamentos de contratos e identidade visual oficial da Saavedra."""

APP_TITLE = "The Nehemizer - Portal Financeiro Saavedra"
APP_SUBTITLE = "Equalização, auditoria e consolidação precisa para contratos financeiros e materiais hospitalares."
APP_VERSION = "1.2.0"
APP_ICON = "📊"

# Paleta Corporativa Oficial Saavedra
PRIMARY_COLOR = "#DC4405"       # Laranja Oficial Saavedra
ACCENT_COLOR = "#DA291C"        # Vermelho Oficial Saavedra
DARK_NEUTRAL = "#25282A"        # Grafite Escuro Oficial Saavedra
BG_CARD_COLOR = "#F8F9FA"       # Fundo neutro suave
BORDER_COLOR = "#E9ECEF"        # Borda sutil
TEXT_MUTED = "#6C757D"          # Texto de apoio
SECONDARY_COLOR = DARK_NEUTRAL

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

# CSS Customizado Corporativo Refinado
CUSTOM_CSS = f"""
    <style>
        .main-title {{
            color: {PRIMARY_COLOR};
            font-size: 2.0rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 0px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .sub-title {{
            color: {TEXT_MUTED};
            font-size: 0.95rem;
            font-weight: 400;
            margin-bottom: 1.5rem;
            margin-top: 4px;
        }}
        .metric-card {{
            background-color: {BG_CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-left: 4px solid {PRIMARY_COLOR};
            padding: 1.2rem;
            border-radius: 6px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}
        .badge-version {{
            background-color: {DARK_NEUTRAL};
            color: #FFFFFF;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}
        .stButton>button {{
            border-radius: 4px;
            font-weight: 600;
            letter-spacing: 0.3px;
        }}
        div[data-testid="stMetricValue"] {{
            color: {DARK_NEUTRAL};
            font-weight: 700;
        }}
    </style>
"""
