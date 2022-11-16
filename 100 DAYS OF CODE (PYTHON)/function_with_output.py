

# functions with outputs

def format_name(f_name,l_name):
    """ used to format a name"""
    if f_name == "" or l_name == "":
        return "no entry of names"


    formatted_f_name =  f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}" 

print(format_name(input("what is your first name?\n"),input("what is you last name?\n")))

# name = "alfred"
# print(name[0].capitalize() + name[1:])






































