#---------------------------------------------------- Peremennue -------------------------------------------------------
# Peremennue ne dolznu nachinatsa na chufru i peremennue ne dolznu imet simvolu @%$%#^%&^*(
# V imeni peremennoi razrewaetsa vukorustovyvat niznee podchirkivanie _
# Peremennue chystvitelnu k rehistry toest rest i Rest eto dve raznue peremennue
# num_1 = int(input("Enter first numbre: "))    # zdes proisxodit prevedenie k int, ptomu chto method input() vozvrawchaet string
# num_2 = int(input("Enter second numbre: "))
# result = num_1 + num_2
# result += 5        # ravnosilno result = result + 5, i tozesamoe mozn delat s  /=  *=  -=  %=
# print("Result is: ", result)
#--------------------------------
# Rest *= 5 # Owibka,  peremennaia Rest ne proinicializirovanaia
#-------------------------------
# Rest = 0
# Rest *= 5   #  a tak nety owibki, potomy chto peremennanya proinicializiroavanaia
#--------------------------------
# ochen interesnoe povedenie, ymnazenie strok
# rest = input("Enter something: ")
# rest *= 5
# rest /= 5    # Error
# print(rest)

# num_1 = input("Enter first numbre: ")
# num_2 = float(input("Enter second numbre: "))
# result = float(num_1) + num_2
# print("Result is: ", result)

# num_1 = input("Enter first numbre: ")
# num_2 = str(input("Enter second numbre: "))
# result = str(num_1) + num_2
# print("Result is: ", result)

# takim sposobom mozno ydalit peremennyy, s pomowchy del
# del result;

# first_name = "Rebeca"
# last_name = "Chaplin"
# full_name = first_name + " " + last_name
# age = 34

# print(full_name)
# print(full_name + age)  # zdes error
# Chtobu nebulo owibki nado zdelat konvertaciy v string s pomowchy str() funcion
# print(full_name + " " + str(age))

# name = input("What is you name?")
# print("Hello " , name)

# x = float(input("Enter your first number:"))
# y = float(input("Enter your second number:"))

# operation = input("Enter your operation...")

# result = None

# if operation == "+":
#     result = x + y
# elif operation == "-":
#     result = x - y
# elif operation == "*":
#     result = x * y
# elif operation == "/":
#     result = x / y
# else:
#     print("Unsopported operation!!!")

# if result is not None:
#     print("Your result =" , result)

# value_1 = 5
# value_2 = value_1
# print(value_1)
# print(value_2)

# value = bool("true")
# value1 = bool("false")
# print(value)
# print(value1)

# radius = 5
# pi = 3.1416
# perimetro = 2 * pi * radius
# print(perimetro)
# area = pi * (radius ** 2)
# print(area)

x, y = 2, 0
print(x)
print(y)