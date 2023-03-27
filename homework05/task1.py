def open_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as datafile:
        phones = datafile.readlines()
    for i in range(len(phones)):
        if phones[i][-1] == '\n':
            phones[i] = phones[i][:-1]
    return phones


def show_phonebook(phones):
    print('\n'.join(phones))


def add_new_phone(phones, contact):
    phones.append(contact)


def delete_contact(phones, phone):
    for i in range(len(phones)):
        if phones[i].split()[1] == phone:
            phones.pop(i)
            break


def find_by_name(phones, name):
    result = []
    for contact in phones:
        if name in contact.split()[0]:
            result.append(contact)
    print('\n'.join(result))


def save_phonebook(phones):
    with open('phonebook.txt', 'w', encoding='utf-8') as datafile:
        datafile.write('\n'.join(phones))
            
    
