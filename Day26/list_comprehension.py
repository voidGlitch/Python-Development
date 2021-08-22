number =[1,2,3]
# new_list =[]
# for n in number:
#    add = n+1
#    new_list.append(add)
# print(new_list)
#in case of this we can use list comprehension

new_list =[n*5 for n in number]
print(new_list)

name= "miku"
new_name=[letters for letters in name]
print(new_name)

new_range =[num*2 for num in range(1,5)]
print(new_range)

test =["miku","alex","angela","maxe","adward","dave"]
short_names =[name for name in test if len(name)<5]
print(short_names)
long_name =[name for name in test if len(name) > 5]
print(long_name)