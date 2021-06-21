import json
from random import random
from typing import Dict

import requests



class SendPrice:

    def __init__(self):
        current = "AC" # "DC"
        base_price = 0.07
        customerDirection = "random IP goes here"
        distance_to_customer = random() * 100 # Kilometers
        kilometerCharge = self.__generateKmCharge(current) # Added % tax per 1000km distance
        prices = self.__generatePrices(base_price, kilometerCharge, distance_to_customer)

        #self.__sendPricesToCustomer(customerDirection,prices)

    def __generatePrices(self, base_price: float, kilometerCharge: float, distance_to_customer: float ) -> Dict[str, float]:
        price_of_electricity = {}
        for time in range(60*60*24):
            if time == 0:
                price_of_electricity[str(time)] = self.__electricityPriceGenerator(time, base_price)+kilometerCharge*distance_to_customer
            else:
                price_of_electricity[str(time)] = self.__electricityPriceGenerator(time, price_of_electricity[ str(time-1) ])+kilometerCharge*distance_to_customer
        return price_of_electricity

    def __electricityPriceGenerator(self, time: int, last_price: float) -> float:
        if time < 60*60*7:
            return last_price - last_price*0.000000793650794
        elif 60 * 60 * 7 <= time < 60 * 60 * 16:
            return last_price + last_price * 0.0000009259259
        elif 60 * 60 * 16 <= time < 60 * 60 * 18:
            return last_price + last_price * 0.0000208333333
        elif 60 * 60 * 18 <= time < 60 * 60 * 20:
            return last_price - last_price * 0.0000208333333
        elif 60 * 60 * 18 <= time < 60 * 60 * 20:
            return last_price - last_price * 0.0000027027027

    def __generateKmCharge(self, current: str) -> float:
        if current == "AC":
            return .07/1000
        elif current == "DC":
            return .03/1000
        else:
            return 0
    def __sendPricesToCustomer(self, direction: str, prices: Dict[str, float]):
        response = requests.post(direction, json.dumps(prices))
