class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

r1 = Rectangle(5, 3)
print(r1.area())




class ScoreBoard:
    def __init__(self, score):
        self.__score = score
    
    def get_score(self):
        return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())
