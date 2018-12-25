from survey import AnonymousSurvey
import unittest
class TestAnonmyousSurvey(unittest.TestCase):
	def test_store_single_response(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)
		
	def test_store_three_responses(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question) # yahan hamen har test k method me instance define karna parega(agar ham ye nahei chahte to ham setUp() method use karenge
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)
			
		for response in responses:
			self.assertIn(response, my_survey.responses)

unittest.main()
