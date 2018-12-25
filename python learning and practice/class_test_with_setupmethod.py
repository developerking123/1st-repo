from survey import AnonymousSurvey
import unittest
class TestAnonmyousSurvey(unittest.TestCase):
	'''self k method me wo attribute or instance banaliye jis ki har
	   method ko testing k liye zaroorat thi or phir unhain har method me call kartlia'''
	def setUp(self): 
		question = "What language did you first learn to speak?" 
		self.my_survey = AnonymousSurvey(question) 
		
	def test_store_single_response(self):
		self.my_survey.store_response('English') 
		self.assertIn('English', self.my_survey.responses)
		
	def test_store_three_responses(self):
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			self.my_survey.store_response(response)
			
		for response in responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
