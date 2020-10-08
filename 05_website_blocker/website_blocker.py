import time
from datetime import datetime as dt

# Paths to files
host_temp = r'.\05_website_blocker\hosts'
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com']

while True:
    # Checking if the time is between 0800 and 1600
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12): 
        print("Not during the work day kiddo")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # Formating the spacing
                    file.write(redirect + " " + website + "\n")
    
    # Reading in file, removing any lines that have Facebook, and then writing it back to the hostfile
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            # Starting at the beginning
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # Cuts everything after the current line
            file.truncate()
        print("Fun hours...")

    time.sleep(5)
    
# with open('..//00_files//vegetables.txt', "a+") as myfile:
#     myfile.write("\nDerek")
#     myfile.seek(0)
#     content = myfile.read()