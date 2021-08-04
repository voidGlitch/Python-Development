from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon" ,["pikachu","chalizard","squirtule"])
table.add_column("type" ,["electric","fire","water"])
table.align = "r"
print(table)