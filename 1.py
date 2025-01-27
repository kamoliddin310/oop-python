class Talaba:

    def __init__(self, ism,familiya,yoshi):
        self.ism = ism
        self.last_name = familiya
        self.age = yoshi


    def get_name(self):
        return self.ism
    
    def tanishnitirish(self):
        return f"ismim {self.ism} {self.last_name} tug'ilgan yilim {self.age}"

    def yoshim(self):
        return f"{self.age}"
    
    def get_age(self, yil):
        return yil - self.age
    
    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith('__') is False]

    

talaba = Talaba("Slohiddin", "Bilmayman", 2000)
# a = int(input("hozirgi yilni kiriting --> "))
# print(talaba.tanishnitirish())
# print(talaba.get_age(a))
# print(dir(Talaba))
print(Talaba.see_methods(talaba))