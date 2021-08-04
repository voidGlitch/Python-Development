path = 3
def game():
    def enemies():
       enemies = 5
       print(f"number of enemies = :{enemies}")     #local 
       print(f"number of path = :{path}")           #global
    enemies()
game()