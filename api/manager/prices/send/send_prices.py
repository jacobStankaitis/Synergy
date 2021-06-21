import sqlite3
import socket
import json


class ManagerPricesSender:
    def __init__(self):
        receivers = [{'ip': '1.1.1.1', 'port': '123123'}, {'ip': '0.0.0.0', 'port': '123'}]
        conn = sqlite3.connect('Prices.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Prices''')
        data = c.fetchall()
        #for x in data:
        # self.__sendPricesToCustomer(receivers['ip'], data , receivers['port'])

    def dict_from_row(row):
        return dict(zip(row.keys(), row))
    def __sendPricesToCustomer(self, direction: str, data, port: str):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((direction, port))
        s.listen(10)
        c, addr = s.accept()
        f = (data).encode()
        c.send(f)
        c.close()