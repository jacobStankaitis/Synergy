import sqlite3
import socket




class ManagerPricesReceiver:
    def __init__(self):
        MANAGER_PUBLIC_IP = "0.0.0.0"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((MANAGER_PUBLIC_IP, 12345))
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

        conn = sqlite3.connect('Prices.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE Prices ( price_id INTEGER PRIMARY KEY, provider TEXT NOT NULL, price TEXT NOT NULL, time TEXT NOT NULL, locationLat TEXT NOT NULL, locationLon TEXT NOT NULL)''')
        conn.commit()
