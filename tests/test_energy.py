
import unittest

from modules.energy.consumption import calculate_consumption, calculate_cost
from modules.energy.solar import (
    calculate_panel_generation,
    calculate_required_panels,
    calculate_solar_results,
)
from modules.energy.comparison import compare_energy_sources
from modules.energy.recommendations import generate_recommendations


class TestEnergy(unittest.TestCase):

    def test_calculate_consumption(self):
        result = calculate_consumption(1000, 5, 30)
        self.assertEqual(result, 150)

    def test_calculate_cost(self):
        result = calculate_cost(150, 0.85)
        self.assertAlmostEqual(result, 127.50)

    def test_calculate_panel_generation(self):
        result = calculate_panel_generation(550, 5, 0.8)
        self.assertAlmostEqual(result, 66)

    def test_calculate_required_panels(self):
        result = calculate_required_panels(150, 550, 5, 0.8)
        self.assertEqual(result, 3)

    def test_calculate_solar_results(self):
        result = calculate_solar_results(
            150, 3, 550, 5, 0.8, 0.85
        )
        self.assertIn("generation", result)
        self.assertIn("energy_offset", result)
        self.assertIn("savings", result)
        self.assertIn("coverage", result)

    def test_compare_energy_sources(self):
        result = compare_energy_sources(150, 0.85, 50, 15)
        self.assertIn("convencional", result)
        self.assertIn("solar", result)
        self.assertIn("eficiente", result)

    def test_generate_recommendations(self):
        result = generate_recommendations(150, 127.50)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
