def name(fname,lname):
    if fname=="" or lname=="":
        return "you didn't provide valid input"

    formatted_fname=fname.title()
    formatted_lname=lname.title()
    return f"{formatted_fname} {formatted_lname}"

fname=input("enter first name\n")
lname=input("enter last name\n")
full_name= name(fname,lname)
print(full_name)