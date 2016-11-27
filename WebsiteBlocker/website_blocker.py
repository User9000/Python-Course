

#this program will prevent you from accessing the sites in the website_list
import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path='/etc/hosts'
redirect='127.0.0.1'

website_list=['www.facebook.com','facebook.com','www.outlook.com','www.cnn.com','www.nytimes.com','www.aristeguinoticias.com','www.lacronica.com']

#to run your program as a daemon
while True:
    #if dt(dt.now().year, dt.now().month, dt.now().day, 0) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,1):
       if dt(dt.now().year, dt.now().month, dt.now().day, 17) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass 
                else:
                    file.write(redirect+"  "+website+"\n")
                  
       else:
        #read all lines of the files/ this will move the pointer to the last line
        with open(hosts_path,'r+') as file:
            #get all lines as a list ans pass them to content variable
            content=file.readlines()
            #take the pointer back to the beginning
            file.seek(0)
            #iterate through the list
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            #erase everything below the pointer
            file.truncate()
        print("Non working hours...")


       
    
       time.sleep(5)