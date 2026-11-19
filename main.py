
import streamlit as st
import pandas as pd

from modules.energy.consumption import (
    calculate_consumption,
    calculate_cost
)

from modules.energy.solar import (
    calculate_required_panels,
    calculate_solar_results
)

from modules.energy.comparison import compare_energy_sources

from modules.energy.recommendations import generate_recommendations


# ==========================================
# CONFIGURAÇÃO DA APLICAÇÃO
# ==========================================

st.set_page_config(
    page_title="Citizen Assist AI",
    page_icon="⚡",
    layout="wide"
)


# ==========================================
# IDENTIDADE VISUAL
# ==========================================

st.title("⚡ Citizen Assist AI")

st.subheader(
    "Sistema inteligente de análise e eficiência energética"
)

st.write(
    "Monitore seu consumo, estime seus custos e "
    "descubra alternativas sustentáveis para sua residência."
)

st.divider()


# ==========================================
# MENU LATERAL
# ==========================================

st.sidebar.title("Menu principal")

opcao = st.sidebar.radio(
    "Selecione uma opção:",
    [
        "Início",
        "Consumo de energia",
        "Energia solar",
        "Comparação",
        "Recomendações"
    ]
)


# ==========================================
# DADOS DE ENTRADA
# ==========================================

st.sidebar.divider()
st.sidebar.subheader("Dados da residência")

tariff = st.sidebar.number_input(
    "Tarifa de energia (R$/kWh)",
    min_value=0.01,
    value=0.85,
    step=0.05
)

panel_power = st.sidebar.number_input(
    "Potência do painel solar (W)",
    min_value=100,
    value=550,
    step=50
)

sun_hours = st.sidebar.number_input(
    "Horas de sol por dia",
    min_value=1.0,
    max_value=12.0,
    value=5.0,
    step=0.5
)

efficiency = st.sidebar.slider(
    "Eficiência do sistema solar",
    min_value=0.50,
    max_value=1.00,
    value=0.80,
    step=0.05
)

efficiency_percentage = st.sidebar.slider(
    "Redução estimada por eficiência energética (%)",
    min_value=0,
    max_value=50,
    value=15,
    step=5
)


# ==========================================
# CÁLCULO DO CONSUMO
# ==========================================

st.sidebar.divider()
st.sidebar.subheader("Equipamento elétrico")

power = st.sidebar.number_input(
    "Potência do equipamento (W)",
    min_value=1,
    value=1000,
    step=100
)

hours_per_day = st.sidebar.number_input(
    "Horas de utilização por dia",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

days_per_month = st.sidebar.number_input(
    "Dias de utilização por mês",
    min_value=1,
    max_value=31,
    value=30
)


# ==========================================
# PROCESSAMENTO DOS DADOS
# ==========================================

consumption = calculate_consumption(
    power,
    hours_per_day,
    days_per_month
)

monthly_cost = calculate_cost(
    consumption,
    tariff
)

panel_count = calculate_required_panels(
    consumption,
    panel_power,
    sun_hours,
    efficiency
)

if panel_count > 0:
    solar = calculate_solar_results(
        consumption,
        panel_count,
        panel_power,
        sun_hours,
        efficiency,
        tariff
    )
else:
    solar = {
        "generation": 0,
        "energy_offset": 0,
        "savings": 0,
        "coverage": 0
    }

solar_percentage = min(solar["coverage"], 100)

comparison = compare_energy_sources(
    consumption,
    tariff,
    solar_percentage,
    efficiency_percentage
)

recommendations = generate_recommendations(
    consumption,
    monthly_cost
)


# ==========================================
# TELA INICIAL
# ==========================================

if opcao == "Início":

    st.header("Painel de controle")

    st.write(
        "Bem-vindo ao Citizen Assist AI! "
        "Acompanhe os principais indicadores energéticos."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Consumo mensal",
        f"{consumption:.2f} kWh"
    )

    col2.metric(
        "Custo estimado",
        f"R$ {monthly_cost:.2f}"
    )

    col3.metric(
        "Painéis necessários",
        f"{panel_count}"
    )

    st.divider()

    st.subheader("Resumo energético")

    st.info(
        "Utilize o menu lateral para acessar os cálculos, "
        "simulações e recomendações do sistema."
    )


# ==========================================
# CONSUMO DE ENERGIA
# ==========================================

elif opcao == "Consumo de energia":

    st.header("Consumo de energia")

    col1, col2 = st.columns(2)

    col1.metric(
        "Consumo mensal",
        f"{consumption:.2f} kWh"
    )

    col2.metric(
        "Custo mensal estimado",
        f"R$ {monthly_cost:.2f}"
    )

    st.subheader("Informações utilizadas")

    st.write(f"Potência: {power} W")
    st.write(f"Horas por dia: {hours_per_day}")
    st.write(f"Dias por mês: {days_per_month}")
    st.write(f"Tarifa: R$ {tariff:.2f}/kWh")

    st.success(
        "Cálculo de consumo realizado com sucesso!"
    )


# ==========================================
# ENERGIA SOLAR
# ==========================================

elif opcao == "Energia solar":

    st.header("Simulação de energia solar")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Painéis necessários",
        f"{panel_count}"
    )

    col2.metric(
        "Geração mensal",
        f"{solar['generation']:.2f} kWh"
    )

    col3.metric(
        "Consumo atendido",
        f"{solar['coverage']:.1f}%"
    )

    st.divider()

    st.subheader("Economia estimada")

    st.metric(
        "Economia mensal",
        f"R$ {solar['savings']:.2f}"
    )

    st.write(
        f"Potência de cada painel: {panel_power} W"
    )

    st.write(
        f"Horas de sol por dia: {sun_hours}"
    )

    st.write(
        f"Eficiência do sistema: {efficiency * 100:.0f}%"
    )


# ==========================================
# COMPARAÇÃO DE ALTERNATIVAS
# ==========================================

elif opcao == "Comparação":

    st.header("Comparação de alternativas energéticas")

    st.write(
        "Compare o consumo e o custo estimado "
        "de três alternativas."
    )

    st.subheader("Conheça as alternativas energéticas")

    with st.expander("⚡ Energia convencional"):
            st.write(
                "É a eletricidade fornecida pela rede de distribuição "
                "que atende à residência."
            )
            st.write(
                "**Vantagem:** não exige a instalação de um sistema "
                "próprio de geração."
            )
            st.write(
                "**Limitação:** o consumidor continua sujeito às "
                "tarifas e condições de fornecimento."
            )

    with st.expander("☀️ Energia solar"):
            st.write(
                "Utiliza painéis fotovoltaicos para transformar "
                "a luz solar em eletricidade."
            )
            st.write(
                "**Vantagem:** pode reduzir o consumo de energia "
                "proveniente da rede elétrica."
            )
            st.write(
                "**Limitação:** depende das condições de instalação, "
                "incidência solar e investimento inicial."
            )

    with st.expander("💡 Eficiência energética"):
            st.write(
                "Consiste em utilizar a energia de maneira mais "
                "eficiente, reduzindo desperdícios."
            )
            st.write(
                "**Vantagem:** pode ser aplicada com mudanças de "
                "hábitos e equipamentos mais eficientes."
            )
            st.write(
                "**Limitação:** a economia depende dos hábitos "
                "e das características dos equipamentos."
            )

    st.divider()

    dados = {
        "Alternativa": [
            "Convencional",
            "Energia solar",
            "Eficiência energética"
        ],
        "Consumo mensal (kWh)": [
            comparison["convencional"]["consumo"],
            comparison["solar"]["consumo"],
            comparison["eficiente"]["consumo"]
        ],
        "Custo mensal (R$)": [
            comparison["convencional"]["custo"],
            comparison["solar"]["custo"],
            comparison["eficiente"]["custo"]
        ]
    }

    df = pd.DataFrame(dados)

    st.subheader("Tabela comparativa")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Comparação de custos")

    grafico_custos = df.set_index("Alternativa")[
        ["Custo mensal (R$)"]
    ]

    st.bar_chart(grafico_custos, horizontal=True)

    st.subheader("Comparação de consumo")

    grafico_consumo = df.set_index("Alternativa")[
        ["Consumo mensal (kWh)"]
    ]

    st.bar_chart(grafico_consumo)

    st.success(
        "Comparação concluída! Os resultados representam "
        "estimativas calculadas a partir dos dados informados."
    )


# ==========================================
# RECOMENDAÇÕES
# ==========================================


elif opcao == "Recomendações":
    st.header("🌎 Recomendações sustentáveis")

    st.write(
        "Informe os dados da sua residência para receber "
        "recomendações personalizadas de economia de energia."
    )

    st.divider()

    st.subheader("Dados do consumo residencial")

    consumo = st.number_input(
        "Consumo mensal (kWh)",
        min_value=0.0,
        value=300.0,
        step=10.0,
    )

    tarifa = st.number_input(
        "Tarifa de energia (R$/kWh)",
        min_value=0.01,
        value=0.80,
        step=0.05,
        format="%.2f",
    )

    # Calcula o custo mensal estimado
    custo_mensal = calculate_cost(consumo, tarifa)

    st.metric(
        "Custo mensal estimado",
        f"R$ {custo_mensal:.2f}"
    )

    # Gera recomendações com base nos dados informados
    recommendations = generate_recommendations(
        consumo,
        custo_mensal
    )

    st.divider()
    st.subheader("Recomendações personalizadas")

    for i, recommendation in enumerate(recommendations, start=1):
        st.info(f"{i}. {recommendation}")

    st.divider()
    st.subheader("Energia renovável")

    st.write(
        "Avalie a viabilidade de instalar painéis solares "
        "e considere as condições da sua residência."
    )

    st.caption(
        "As recomendações são orientações gerais. "
        "A economia real depende dos hábitos de consumo, "
        "dos equipamentos e das condições da residência."
    )



# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.caption(
    "Citizen Assist AI | Global Solution 2026.2"
)
