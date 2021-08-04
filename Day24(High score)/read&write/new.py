#File = open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt")
# another way to open file is 

# with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt") as File:
#  content = File.read()  # returns the contents of the file
#  print(content)
#  # File.close() in this we do not need that as file is closed 



with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt", mode="w") as File:
 '''by default the mode is readable only so we have to modify it and make it write'''
 File.write("some text.")  # delete all the prev content and overwrite in it