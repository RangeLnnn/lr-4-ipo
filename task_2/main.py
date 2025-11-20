how_many=int(input("как много чисел вы хотите внести в список: "))
some_list=[]
counter=0
while counter<how_many:
    print(f"Введите {counter+1} элемент списка")
    user_input=int(input(">>>>>"))
    some_list.append(user_input)
    counter+=1
print("исходный список - ",some_list)
some_list=[i**2 for i in some_list]
print("список с числами в квадрате - ",some_list)