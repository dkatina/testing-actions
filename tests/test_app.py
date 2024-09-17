import unittest
from faker import Faker
from app import app



class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #importing our app to be used as the app for this testcase

    def test_sum_stub(self):
        #Payload contains 2 nums num1 and num2
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/sum', json=payload) #sending a post request to our app, at endpoint /sum with defined payload
        data = response.json
        self.assertEqual(data['result'],5)

    def test_sum_mock(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.json
        self.assertEqual(data['result'], num1+num2)

if __name__ == '__main__':
    unittest.main()