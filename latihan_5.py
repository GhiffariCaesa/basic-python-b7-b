#class
#class myclass:
    #x=5
#p1 = myclass()
#print(p1.x)

#__init__
class Person:
    def __init__(self, input_name, input_age, input_hobby):
        self.name = input_name
        self.age = input_age
        self.hobby = input_hobby
    def greet(self):
        print("Halo namaku",self.name)
    def umur(self):
        print("Saat ini saya berumur",self.age)
    def hobi(self):
        print("Aku memiliki hobi",self.age)            
user = Person("Ghiffari", 21, "Membaca buku")
user.greet()
user.umur()
user.hobi()