# Error Handling
try:
## File doesn't exist
    file = open("orders.txt")

## Instead of an error you get the below message
# except
#     print('OMG YOU BIFFED IT')
## Can make error messages for specific error and save original error message as placeholder (errormessage)
except FileNotFoundError as errormessage:
    print('Check file name &/or path - file cannot be found')
    print(errormessage)

# Opening and reading files
file = open("order.txt")
lines = file.readlines()
for line in lines:
    print(line.strip('\n'))

# Closing files
file.close() # This closes the file, so that it can be used by other programs

# Creating a function to open file, read and print lines and the close file
def open_close(file_name):
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        print(line.strip('\n'))
    file.close()
## Call function
open_close("order2.txt")

# Function for opening and closing file with error handling without having to specific file.closer() because of 'with open'
def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))
    except FileNotFoundError as error:
        print('Check your file')
        print(error)
    # Do something as function ends
    finally:
        print('Program closing! Time to go home chap')
## Call function
open_print_close("order.txt")


# Writing to file

