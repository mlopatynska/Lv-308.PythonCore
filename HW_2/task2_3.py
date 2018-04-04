variable_1 = str(raw_input("The first variable is...\n"))
variable_2 = str(raw_input("The second variable is...\n"))
variable_1 = variable_1 + "!@!@!" + variable_2
variable_2 = variable_1[:variable_1.find("!@!@")]
variable_1 = variable_1[variable_1.find("!@!@")+5:]

print(variable_1)
print(variable_2)

