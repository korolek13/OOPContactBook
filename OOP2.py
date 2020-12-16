class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print(self.name, self.phone)
    def say(self):
        print('Hello')
    

class Friend(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address
    
    def show(self):
        print(self.phone, self.name, self.address)
    
    def say(self):
        if self.name == 'Дмитрий':
            super().say()
        else:
            print('Я не Дмитрий')
        
user = User('Геннадий', '2676')
friend = Friend('Дмитрий', '7626', '56')
friend2 = Friend('Никита', '1341', 'da')

user.show()
friend.show()
friend.say()
friend2.say()