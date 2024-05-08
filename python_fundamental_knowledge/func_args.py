# def user_info(name, age, city):
#     '''This function prints name, age and city
#     from an argument provided to the function'''
#
#     print("{} is {} years old and lives in {}".format(name, age, city))
#
# user_info("Janet", 25, "Nairobi")
# user_info( 30, "Kampala")

#keyword arguments
def user_info(name,age=0,city="Tucson"):
    '''This function prints name, age and city
    from an argument provided to the function'''

    print("{} is {} years old and lives in {}".format(name, age, city))

user_info("Micah")
user_info(age=25,name="Micah")

# *args :allows for unlimited variables to be passed
# to a function without defining them ahead of time
def add(*args):
    print(sum(args))

add(1,2,3,4,5,6,7,8,9,10)



# **kwargs
# allows for unlimited keyword arguments to be passed
# into a function without defining them ahead of time
def application(**kwargs):
    print(kwargs)

application(fname="Jess", lname="Ingrass", email="mail@mail.com")


# Combining arg types
# All three argument types can be used in a single function
# They must be used in order: formal positional arguments, *args, **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}".format(fname, lname,company,email))

application("Jess", "Ingrass", "mail@mail.com",
            "TeachCode.org", 75000, hire_date = "September 1, 2020")
