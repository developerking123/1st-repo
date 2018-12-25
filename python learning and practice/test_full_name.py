import unittest
from name_function import formatted_name
class Test_function(unittest.TestCase):
	def test_all_letter_in_lowercase(self):
		full_name = formatted_name("abdul", "saboor")
		self.assertEqual(full_name, "Abdul Saboor")
	
	def test_all_letter_in_uppercase(self):
		full_name = formatted_name("ABDUL", "SABOOR")
		self.assertEqual(full_name, "Abdul Saboor")
	
	def test_spaces_in_firstandlast_names(self):
		full_name = formatted_name(" ABDUL ", " SABOOR ")
		self.assertEqual(full_name, "Abdul Saboor")

unittest.main()
