
def calculate_consumption(
    power,
    hours_per_day,
    days_per_month
):
    """
    Calcula o consumo mensal de energia
    de um equipamento em kWh.
    """

    consumption = (
        power * hours_per_day * days_per_month
    ) / 1000

    return consumption


def calculate_cost(consumption, tariff):
    """
    Calcula o custo estimado do consumo.
    """

    return consumption * tariff
