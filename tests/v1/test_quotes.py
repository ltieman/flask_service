from tests.base_case import BaseTestCase
import json
from app.v1.component import Character
import json

class TestQuotes(BaseTestCase):
    def test_get_quote_for_gandalf(self):
        """
        test to check the endpoint to ensure that the the endpoint returns the correct data
        :return:
        """
        response = self.client.get(f"/v1/quotes/", headers=self.headers, query_string={"name": "Gandalf"})
        self.assertEqual(response.status_code, 200, response.data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIs(type(data['quote']), str)


class TestCharectorComponent(BaseTestCase):
    def test_get(self):
        """
        test the get method of the base class
        """
        with self.app.app_context():
            response = Character().get({"name": "Gandalf"})
            self.assertIs(type(response), dict)
            self.assertIn("docs", response)
            self.assertEqual(response['docs'][0]['name'], "Gandalf")
            self.assertIs(type(response['docs'][0]['_id']), str)
            self.assertIs(type(response['docs'][0]['race']),str)
            self.assertIs(type(response['docs'][0]['gender']),str)
            self.assertIs(type(response['docs'][0]['birth']),str)

    def test_get_subroute(self):
        """
        test the get sub route method of the base class
        """
        with self.app.app_context():
            name_response = Character().get({"name": "Gandalf"})
            id = name_response['docs'][0]['_id']
            response = Character().get_sub_route_by_id("quote", id)
            self.assertIs(type(response), dict)
            self.assertIn("docs", response)
            for resp in response['docs']:
                self.assertIs(type(resp['dialog']), str)
                self.assertIs(type(resp['movie']), str)
                self.assertIs(type(resp['character']), str)
                self.assertIs(type(resp['_id']), str)

    def test_get_charector_quote(self):
        """
        test the get charector quote method of the charector class
        this is the same method that does most everything in the endpoint test
        """
        with self.app.app_context():
            quote = Character().get_character_quote("Gandalf")
            self.assertIs(type(quote), str)
            quote = json.loads(quote)
            self.assertIs(type(quote['quote']), str)


