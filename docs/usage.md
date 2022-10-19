# Usage

```py
"""
This is a Demo file to help you get started.
"""

# Load the Important Modules
import os

from dotenv import load_dotenv

from .ripledd import Ripledd

# Loading the Enviroment Variables
load_dotenv()

# Assigining then a constant
EMAIL = os.environ.get("RIPLEDD_EMAIL")
PASSWORD = os.environ.get("RIPLEDD_PASSWORD")

# Creating a Ripledd Object
ripledd = Ripledd(email=EMAIL, password=PASSWORD)

# Printing the success
print(ripledd.create_post("The Post from the API").ok)
```