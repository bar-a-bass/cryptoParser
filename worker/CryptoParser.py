import requests
import json
from models import MarketModel
from models import FeeModel, FeeExtensionModel


class Parser:
    @staticmethod
    def get_market_data(market, limit=50):
        response = requests.get(f'https://garantex.io/api/v2/trades?market={market}&limit={limit}')
        dict_data = json.loads(response.text)
        market_model = MarketModel.MarketModelClass(dict_data[0]["id"], dict_data[0]["price"], dict_data[0]["volume"],
                                                    dict_data[0]["funds"], dict_data[0]["market"],
                                                    dict_data[0]["created_at"])
        return market_model

    @staticmethod
    def get_fee():
        response = requests.get(f'https://garantex.io/api/v2/fees/trading')
        fee_dict = json.loads(response.text)
        fee_ask_array = []
        fee_bid_array = []

        for i in fee_dict[6]['ask_fee']:
            fee_ask_model = FeeExtensionModel.FeeExtensionModelClass(i["type"], i["value"])
            fee_ask_array.append(fee_ask_model)
        for n in fee_dict[6]['bid_fee']:
            fee_bid_model = FeeExtensionModel.FeeExtensionModelClass(n["type"], n["value"])
            fee_bid_array.append(fee_bid_model)

        fee_model = FeeModel.FeeModelClass(fee_dict[6]['market'], fee_dict[6]['unit'],
                                           fee_ask_array, fee_bid_array)

        return fee_model
