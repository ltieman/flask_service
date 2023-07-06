from flask import current_app
import requests
from typing import Union
from marshmallow import Schema


class BaseIntegration:
    base_url: str
    schema: Schema

    def __init__(self):
        #set headers
        self.headers = {"Authorization": f"Bearer {current_app.config['ONE_DEV_API_KEY']}"}

    def get(self, query_params:dict)->dict:
        """
        get data from the base url
        :param query_params:
        :return: dict
        """

        response = requests.get(f"{self.base_url}", params=query_params, headers=self.headers)
        return response.json()

    def get_sub_route_by_id(self, sub_route:str,id: Union[str, int]):
        """
        get sub route by id off the base url
        :param sub_route:
        :param id: id for the resource, can be string or int
        :return: dict
        """
        response = requests.get(f"{self.base_url}/{id}/{sub_route}", headers=self.headers)
        return response.json()


