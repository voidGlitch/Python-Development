#File = open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt")
# another way to open file is 

# with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt") as File:
#  content = File.read()  # returns the contents of the file
#  print(content)
#  # File.close() in this we do not need that as file is closed 



# with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt", mode="w") as File:
#  '''by default the mode is readable only so we have to modify it and make it write'''
#  File.write("some text.")  # delete all the prev content and overwrite in it

# with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_text.txt", mode="a") as File:
#  '''by default the mode is readable only so we have to modify it and make it write or append(a)'''
#  File.write("some text with some append mode.")  # append the text

with open("E:\\python on udemy\\Day24(High score)\\read&write\\new_file.txt", mode="w") as File:
 '''by default the mode is readable only so we have to modify it and make it write or append(a)'''
 File.write("some text with some append mode.")  # append the text
 # it will create new file if we don't have the existing file there automatically