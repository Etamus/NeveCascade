# tests/test_model.py

import unittest
from src.model import NeveCascadeModel

class TestNeveCascadeModel(unittest.TestCase):
    def test_forward_shape(self):
        model = NeveCascadeModel()
        # Entrada fictícia
        x = [0] * 512
        y = model.forward(x)
        self.assertEqual(len(y), 512)

if __name__ == '__main__':
    unittest.main()
