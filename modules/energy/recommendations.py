def generate_recommendations(consumption, monthly_cost):
    """
    Gera recomendações para reduzir o consumo de energia.
    """

    recommendations = []

    if consumption > 300:
        recommendations.append(
            "Reduza o tempo de uso de equipamentos de alto consumo."
        )
    else:
        recommendations.append(
            "Continue acompanhando seu consumo mensal de energia."
        )

    recommendations.append(
        "Prefira lâmpadas LED e equipamentos com boa eficiência energética."
    )

    recommendations.append(
        "Desligue equipamentos quando não estiverem em uso."
    )

    if monthly_cost > 200:
        recommendations.append(
            "Avalie alternativas para reduzir sua conta de energia."
        )

    recommendations.append(
        "Considere estudar a viabilidade de instalar painéis solares."
    )

    return recommendations