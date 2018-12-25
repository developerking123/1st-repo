from name_function import formatted_name
ch = True
while ch:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(formatted_name(first_name, last_name))
    choice = input("Do you want to continue press y for yes any other key for no: ")
    if choice != 'y':
        ch = False
        
