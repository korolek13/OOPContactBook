class Contact:
    def __init__(self, name, phone, birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        print('Создан новый контакт')
    
    def show_info(self):
        print(f'{self.name} - phone: {self.phone}, birthday: {self.birthday}')
        
    def __str__(self):
        return self.name
        
Mike = Contact('Mihail Bulgakov', '20327', '15.05.1891')
Vlad = Contact('Vladimir Mayakovsky', '7388', '19.07.1893')
Max = Contact('Maksim Savelyev', '7388', '19.07.1893')


Mike.phone = '27'

Mike.show_info()
Vlad.show_info()
Max.show_info()

print(Max)