#number 7a
class Team:
    def __init__(self, name, year, city):
        self.name = name
        self.year = year
        self.city = city
        self.wins = 0
        self.losses = 0

    def __str__(self):
        return "{} {}: {} wins, {} losses".format(self.year, self.name, self.wins, self.losses)

    def wonGame(self):
        self.wins += 1

    def lostGame(self):
        self.losses += 1

    def getWinPercent(self):
        if self.wins == 0:
            return 0
        else:
            return self.wins / (self.wins + self.losses) * 100

Class=Team("Arsenal", "2018", "London")
print(Class)
Class.wonGame()
print(Class)
Class.lostGame()
print(Class)
print(Class.getWinPercent())


# Question 2\n"


class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Width: {}, Height: {}, Area: {}, Perimeter: {}".format(self.width, self.height, self.getArea(), self.getPerimeter())

width = 3
height = 30
width2 = 4.5
height2 = 45.5
rectanle1=Rectangle(width, height)
rectanle2=Rectangle(width2, height2)
print(rectanle1)
print(rectanle2)
print("Ratio: {}".format(rectanle1.getArea() / rectanle2.getArea()))

