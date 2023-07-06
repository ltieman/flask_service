from .base import BaseIntegration
from flask import Blueprint, request
from random import choice
from marshmallow import Schema, fields

class LOTRQuote(Schema):
    quote = fields.String(required=True)


class Character(BaseIntegration):
    base_url = "https://the-one-api.dev/v2/character"
    schema = LOTRQuote()

    def get_character_quote(self,character:str)->str:
        """
        get character quote of LOTR character by name
        :param character:
        :return:
        """
        #pull the charector from the query params
        query_params = {"name": character}
        #get the charector data from the api
        character_data = self.get(query_params)
        #get the charector id from the data
        character_id = character_data['docs'][0]['_id']
        #get the quote data from the api
        quote_data = self.get_sub_route_by_id("quote", character_id)
        #get a random quote from the quote data
        quote = choice(quote_data['docs'])['dialog']
        #return the quote
        return LOTRQuote().dumps({"quote": quote})



quote_api = Blueprint('quotes', __name__,url_prefix='quotes')


@quote_api.route('/', methods=['GET'])
def get_quote():
    """
    get quote for LOTR charecter
    :return:
    """
    charecter_name = request.args.get('name')
    return Character().get_character_quote(charecter_name)


