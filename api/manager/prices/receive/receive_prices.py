import sqlite3
import socket
import json


class ManagerPricesReceiver:
    def __init__(self):
        manager_public_ip = "0.0.0.0"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((manager_public_ip, 12345))
        data = str()
        while True:
            m = s.recv(1024)
            data = m
            if m:
                while m:
                    m = s.recv(1024)
                    data += m
                else:
                    break
        dct = json.loads(data)
        conn = sqlite3.connect('Prices.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Prices ( price_id INTEGER PRIMARY KEY, provider TEXT NOT NULL, price TEXT NOT NULL, time TEXT NOT NULL, 
        locationLat TEXT NOT NULL, locationLon TEXT NOT NULL, priceIncreasePer1000km TEXT NOT NULL)''')
        for time in range(60 * 24):
            c.execute(
                '''INSERT INTO Prices VALUES( dct['providerName'] , dct[time], time, dct['factoryLat'], dct['factoryLon'], dct['priceIncreasePer1000km'] )''')
        conn.commit()
