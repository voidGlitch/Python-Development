enemies = 1
# def increase_enemies():
#     # enemies += 1
#     # print(enemies)  doesn't print because it is not defined globally
#     global enemies
#     enemies += 1
#     print(f"{enemies} inside the function")  or you can write
def increase_enemies():
    print(f"enenmies inside the function{enemies}")
    return enemies +1
enemies = increase_enemies()
print(f"{enemies} out")