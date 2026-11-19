
from math import ceil


def calculate_panel_generation(
    panel_power,
    sun_hours,
    efficiency,
    days=30
):
    """
    Calcula a geração mensal estimada de um painel solar.
    Resultado em kWh.
    """

    generation = (
        (panel_power / 1000)
        * sun_hours
        * days
        * efficiency
    )

    return generation


def calculate_required_panels(
    consumption,
    panel_power,
    sun_hours,
    efficiency
):
    """
    Estima a quantidade de painéis necessários
    para atender ao consumo mensal.
    """

    generation_per_panel = calculate_panel_generation(
        panel_power,
        sun_hours,
        efficiency
    )

    if generation_per_panel <= 0:
        return 0

    return ceil(consumption / generation_per_panel)


def calculate_solar_results(
    consumption,
    panel_count,
    panel_power,
    sun_hours,
    efficiency,
    tariff
):
    """
    Calcula geração total, economia estimada
    e percentual do consumo atendido.
    """

    generation_per_panel = calculate_panel_generation(
        panel_power,
        sun_hours,
        efficiency
    )

    total_generation = generation_per_panel * panel_count

    energy_offset = min(consumption, total_generation)

    savings = energy_offset * tariff

    coverage = (
        (energy_offset / consumption) * 100
        if consumption > 0
        else 0
    )

    return {
        "generation": total_generation,
        "energy_offset": energy_offset,
        "savings": savings,
        "coverage": coverage
    }
