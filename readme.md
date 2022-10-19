![Banner](/images/banner.png)

# Ripledd Python

A simple API wrapper made for [Ripledd](https://ripledd.com/center/).

```
pip install ripledd-python
```

```py
# demo.py

# Load the Important Modules
import os

from dotenv import load_dotenv


import Ripledd

# Loading the Enviroment Variables
load_dotenv()

# Assigining them a constant
EMAIL = os.environ.get("RIPLEDD_EMAIL")
PASSWORD = os.environ.get("RIPLEDD_PASSWORD")

# Creating a Ripledd Object
ripledd = Ripledd(email=EMAIL, password=PASSWORD)

# Printing the success
print(ripledd.create_post("The Post from the API").ok)

```

## **Run it**

```ps
PS C:\Users\ripledd\Projects\Bots>python demo.py
```

## **Response**

You will get the following response

![Response](/images/response.jpeg)


*Cheers*