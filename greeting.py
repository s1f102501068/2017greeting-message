def greet(name):
    message = 'Hello, ' + name + '-san!'
    print(message)
    
from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message + "," + name +  "-san!")


greet("Inoue")
print("INIAD")
