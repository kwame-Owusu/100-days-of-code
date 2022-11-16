
#example of how dictionaries work in python
# on the left we have the "key" and on the right the "value, to know what the value we have to call the key




programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
}

#example of calling the key to reveal the value.

# print(programming_dictionary["Bug"])







# adding new items into the dictionary, editing a the value of a key in a dictionary is the same, we just change the values but maintain the same sintax

programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)




# how to wipe an existing dictionary: we can wipe a dictionnary by just assigning the variable to {}, this will wipe all the keys and values inside the dictionary


# looping thorugh a dictionary

# for item in programming_dictionary:
    # print(item)
    # print(programming_dictionary[item])
# this makes it that the for loop catches the values assigned to the keys as well, without this syntax the for loop will only print the keys



# Nesting 

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

travel_log = {
    "France" : {"cities_visited":["Paris","Lille","Dijon"]},
    "Germany" : ["Frankfur","Hamburg","Stuttgart"],
}


# nesting a dictionary in a list




travel_log2 = [
    
    {"country" :  "France", 
    "cities_visited":["Paris","Lille","Dijon"]
    
    },
    
    {"country" : "Germany", 
    "cities_visited" :["Frankfur","Hamburg","Stuttgart"]
    
    },
]

print(travel_log2[0]["cities_visited"])

