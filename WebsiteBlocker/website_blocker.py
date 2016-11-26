

import time
from datetime import datetime as dt


hosts_path='/etc/hosts'
redirect='127.0.0.1'


website_list=['www.facebook.com','facebook.com','www.outlook.com','www.cnn.com','www.nytimes.com','www.aristeguinoticias.com','www.lacronica.com']


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working hours...")

    else:
         print("Non working hours...")
    time.sleep(5)