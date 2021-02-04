import unittest
from src.index import lambda_handler

event = {
    "Details": {
        "ContactData": {
            "ContactId": "dynamodb-unitTestuuid"
            },
        "Parameters": {
                "fname": "testName",
                "lname": "testSubject"
            }
        }
    }

class LambdaAssertionsTest(unittest.TestCase):
    def test_lambda_returns_dictionary(self):
        self.assertIsInstance(lambda_handler(event), dict)
    
    def test_lambda_returns_200(self):
        x = lambda_handler(event)
        statusCode = x['ResponseMetadata']['HTTPStatusCode']
        self.assertEqual(statusCode, 200)

    def test_lambda_doesNotReturn400(self):
        x = lambda_handler(event)
        statusCode = x['ResponseMetadata']['HTTPStatusCode']
        self.assertNotEqual(statusCode, 400)

    def test_lambda_contentLength_greater_than_0(self):
        x = lambda_handler(event)
        content_length = int(x['ResponseMetadata']['HTTPHeaders']['content-length'])
        self.assertGreater(content_length, 0)

    def test_content_length_is_str(self):
        x = lambda_handler(event)
        content_length = x['ResponseMetadata']['HTTPHeaders']['content-length']
        self.assertIsInstance(content_length, str)

    def test_content_length_is_not_str(self):
        x = lambda_handler(event)
        content_length = int(x['ResponseMetadata']['HTTPHeaders']['content-length'])
        self.assertIsNot(type(content_length), str)

    def test_contentType_is_application_x_amz_json_1_0(self):
        x = lambda_handler(event)
        content_type = x['ResponseMetadata']['HTTPHeaders']['content-type']
        self.assertEqual(content_type, 'application/x-amz-json-1.0')

    def test_lambda_retry_attempts_is_0(self):
        x = lambda_handler(event)
        retry_attempts = x['ResponseMetadata']['RetryAttempts']
        self.assertEqual(retry_attempts, 0)

if __name__ == '__main__':
    unittest.main()