import unittest

class Test(unittest.TestCase):
	def setUp(self):
		print("Set up")
	
	def test_output(self):
		print("Test")
		
	def tearDown(self):
		print("Tear down")

if __name__ == "__main__":
	unittest.main()
