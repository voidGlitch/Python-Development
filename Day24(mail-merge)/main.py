#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("E:\\python on udemy\\Day24(mail-merge)\\Input\\Names\\invited_names.txt") as name:
    all_names = name.readlines()
    print(all_names)
    
    
with open("E:\\python on udemy\\Day24(mail-merge)\\Input\\Letters\\starting_letter.txt",mode="r") as file:
    letter =file.read()
    for names in all_names:
        y =names.strip()
        x =letter.replace("[name]",y)
        with open(f"\python on udemy\Day24(mail-merge)\Output\ReadyToSend\example_{y}.txt" , mode ="w") as all_letter:
            all_letter.write(x)