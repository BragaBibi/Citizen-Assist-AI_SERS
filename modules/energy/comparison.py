
def compare_energy_sources(consumption, tariff, solar_percentage, efficiency_percentage):
    """
    Compara três alternativas de consumo energético:
    energia convencional, energia solar e energia eficiente.
    """

    # Energia convencional
    conventional_cost = consumption * tariff

    # Energia solar
    solar_cost = conventional_cost * (1 - solar_percentage / 100)

    # Energia eficiente
    efficient_consumption = consumption * (1 - efficiency_percentage / 100)
    efficient_cost = efficient_consumption * tariff

    return {
        "convencional": {
            "consumo": consumption,
            "custo": conventional_cost
        },
        "solar": {
            "consumo": consumption * (1 - solar_percentage / 100),
            "custo": solar_cost
        },
        "eficiente": {
            "consumo": efficient_consumption,
            "custo": efficient_cost
        }
    }
