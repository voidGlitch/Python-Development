from art import logo 
#add
def add(a,b):
  return a + b
    #sub
def sub(a,b):
  return a - b
    #multiply
def multiply(a,b):
  return a * b
    #divide
def divide(a,b):
  return a/b

operations ={
"+":add,
"-":sub,
"*":multiply,
"/":divide
}
def calculator():
# function = operations["*"]
# function(2,3)  whatever we type here used as the function of the given operator
  print(logo)
  num1 =float(input("what is your first number :"))

  for items in operations:
      print(items)

  conti=1
  while(conti):    
      user = input("what operation do you want to perform :")
      num2 =float(input("what is your next number :"))
      calculation_function = operations[user]
      answer = calculation_function(num1,num2)
      print(f"{num1} {user} {num2} = {answer}")
      
      to_continue= input("do you want to continue the same?Tyoe 'yes'or 'no'")
      if to_continue == "yes":
        num1 = answer
      else:
        conti=0
        calculator()
calculator()