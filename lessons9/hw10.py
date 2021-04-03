import sys



def input_error(func):
    def inner(d):
        try:
            func(d)
        except KeyError:
            print('Please enter the correct command!')
        except ValueError:
            print('Enter user name')
        except IndexError:
            print('Give me name and phone please')
    return inner


@input_error
def Hello_func(d):
    print("How can I help you?")

@input_error
def add_func(list):
    print('Your contact has been added')
    return contacts.setdefault(list[1], list[2])

@input_error
def change_func(list):
    print('Your contact is treason')
    return contacts.update({list[1]: list[2]})

@input_error
def phone_contacts_func(list):
    print('Phone number -', contacts[(list[1])])

@input_error   
def show_all_contacts_func(list):
    for k, v in contacts.items():
        print(k , v)

@input_error
def end_contacts_func(list):
    print("Good bye!")
    sys.exit(0)

@input_error        
def get_handler(operator):
    global d
    d = operator.split(' ')
    if 'show all' in operator or 'good bye' in operator:
        OPERATIONS[d[0]+ ' ' +d[1]](d)
    else:
        OPERATIONS[d[0]](d)


contacts = {}


# 
OPERATIONS = {
    'hello': Hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_contacts_func,
    'show all': show_all_contacts_func,
    'good bye': end_contacts_func,
    'close': end_contacts_func,
    'exit': end_contacts_func,
    '.': end_contacts_func
}

def main():
    while True:
        input_command = input('Enter command: ')
        get_handler(input_command)

    
if __name__ == "__main__":
    main()
#print(contacts)


