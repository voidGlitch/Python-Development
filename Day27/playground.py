# unlimited positional arguments
def add(*args):
 print(args[1])
 sum =0
 for items in args:
  # print(items)
  sum = sum + items
 print(sum)

add(5,3,6,65,21,2,1,5,4,5,456,4,1,2,5,4)