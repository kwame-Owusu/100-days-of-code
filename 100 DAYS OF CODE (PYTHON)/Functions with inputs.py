# the parameter is the name put in the first definition of the function
# the arugument is the "value" passed into the function when called on line 14. argument is the value associated with the parameter, the parameter can be any name.


# Example of a function witha  parameter and an argument being passed in.

# def greet(name):
#      print(f"Hello {name}")
#      print(f"How are you {name}?")
    
# greet("Alfred")




# Function with multiple inputs






# Keyword arguments are when you already specify the value  by assigning the parameters to a value.


def greet_with (name ,location ):
    print(f"Hello {name}")
    print(f"How is it like in {location}")
   

# with keyword arguments the position of the parameters don't matter as the argument has been assigned already hence the position will not cause any issues.

greet_with(location = "Nottingham", name = "Alfred") 
