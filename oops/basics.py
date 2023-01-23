class car:
    # pass #creates an empty class
    def __init__(self,speed,color):
        print(speed)
        print(color)
        print("the __init__ is called")

ford = car(300,"blue")
skoda =car(250,"red")
Audi = car(600,"pink")

# ford.speed=100
# ford.color='red'
# skoda.speed=200
# skoda.color='blue'

# print(ford.speed)
# print(ford.color)