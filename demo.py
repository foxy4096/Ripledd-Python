import os

from dotenv import load_dotenv

from main import Ripledd

# Loading the Enviroment Variables
load_dotenv()

# Assigining then a constant
EMAIL = os.environ.get("RIPLEDD_EMAIL")
PASSWORD = os.environ.get("RIPLEDD_PASSWORD")

# Creating a Ripledd Object
ripledd = Ripledd(email=EMAIL, password=PASSWORD)

# Printing the success
print(ripledd.create_post("The Post from the API").ok)
