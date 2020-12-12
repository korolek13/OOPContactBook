class Contact:
    def __init__(self, name, phone, birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        print('Создан новый контакт')

Mike = Contact('Mihail Bulgakov', '20327', '15.05.1891')
Vlad = Contact('Vladimir Mayakovsky', '7388', '19.07.1893')

def print_contact():
    print(f'{Mike.name} - phone: {Mike.phone}, birthday: {Mike.birthday}')
    print(f'{Vlad.name} - phone: {Vlad.phone}, birthday: {Vlad.birthday}')

Mike.phone = '27'

print_contact()
