class Robot:
    pass

robot1=Robot()
print(robot1)


class Cup:
    color="white"

cup1=Cup()
cup2=Cup()

print(cup1.color)
print(cup2.color)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1 = Student("Aye Aye", 18)
student2 = Student("Min Min", 19)

print(student1.name , student1.age)
print(student2.name , student2.age)

class Member:
    def __init__(self,name,city,age=18):
        self.name=name
        self.city=city
        self.age=age
member1=Member("Nila","yangon")
member2=Member("ko","mandalay",22)
print(member1.name,member1.city,member1.age)
print(member2.name,member2.city,member2.age)

class Pet:
    def __init__(self,name):
      self.name=name

pet1=Pet("Miko")
print(pet1.name)


class Profile:
    def __init__(self,name,age,city):
        self.name=name
        self.age =age
        self.city=city

profile=Profile("Thiri",22,"Bago")
profile.age=21
profile.hobby="drawing"

del profile.city
print(profile.name,profile.age,profile.hobby)

class Car:
    brand="Toyota"

car1=Car()
car2=car1     #**********************
del car1

print(car2.brand)

class Student:
    school="North School"

    def __init__(self,name):
        self.name=name

student1= Student("Aye")

student2= Student("Mya")
Student.school="West School"

print(student1.name,student1.school)

print(student2.name,student2.school)



class Player:
    team= "Blue"

player1=Player()
player2=player1         #**************************
player1.team="Red"
Player.team="Green"

print(player1.team)
print(player2.team)
print(Player.team)

del player1.team
print(player1.team)


class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __str__(self):
        return f"{self.title,self.pages}"

book=Book("Python Basic",120)
print(book)
print(str(book))

class Student:
    def __init__(self,name):
        self.name=name

    # def greet(self):
    #     return f"Hello , {self.name}"     #9****************

    def welcome(self):
        print(f"Hello,{self.name}")
        print("Welcom to class.")

student=Student("Mya")
student.welcome()


class BillCalculator:
    def total(self,price,quantity):
        return price *quantity

    def discount(self,total,amount):
        return total-amount

calulator= BillCalculator()
subtotal=calulator.total(12,3)
final_total=calulator.discount(subtotal,5)

print(subtotal)
print(final_total)


class GamePlayer:
    def __init__(self,name,score=0):
        self.name=name
        self.score=score

    def add_point(self,point):
        self.score += point

    def get_info(self):
        return f"{self.name}: {self.score} point"

player1=GamePlayer("Mya")
player2=GamePlayer("Hal")
player1.add_point(10)
player1.add_point(5)

print(player1.get_info())
print(player2.get_info())


# class Playlist:                     #zzzzzzzzzzzzzzzzzzzzzzzzzz

#     def __init__(self,name):
#         self.name=name
#         self.songs=[]

#     def add_song(self,song):
#         self.songs.append(song)

#     def remove_songs(self,song):
#         if song in self.songs:
#             self.songs.remove(song)

#     def show_info(self):
#         print(f'{self.name}:')
#         for song in self.songs:
#             print(f"-{song}")

# playlist = Playlist("Study")
# playlist.add_song("Sunrise")
# playlist.add_song("MoonLight")
# playlist.remove_songs("Sunrise")
# playlist.show_info()


class Badge:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(self.name)

    def __str__(self):
        return f"Badge:{self.name}"

badge1=Badge("Aye")
badge2=Badge("Mya")
badge1.show()

del Badge.show
print(badge1)
print(badge2)