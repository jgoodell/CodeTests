import unittest


import hex_to_base64


class TestHexBase64(unittest.TestCase):
    def test_success(self):
        assert hex_to_base64.utils.translate('45766964696e74') == 'RXZpZGludA== '
        
