import unittest
from app import create_app, db
from config import config
import json


class TestAPI(unittest.TestCase):
    def setUp(self):
        environment = config["test"]
        self.app = create_app(environment)
        self.client = self.app.test_client()

        self.content_type = "application/json"
        self.path = "http://127.0.0.1:5000/api/v1/jokes"
        self.path_first_joke = self.path + "/1"
        self.path_not_funny_joke = self.path + "/100"

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    # Aux method
    def get_joke_id(self, response):
        data = json.loads(response.data.decode("utf-8"))
        return data["data"]["id"]

    def test_get_all_jokes(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(len(data["data"]), 1)

    def test_get_first_joke(self):
        response = self.client.get(
            path=self.path_first_joke, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 200)

        joke_id = self.get_joke_id(response)
        self.assertEqual(joke_id, 1)

    def test_not_found(self):
        response = self.client.get(
            path=self.path_not_funny_joke, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
