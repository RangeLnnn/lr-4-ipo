how_many=int(input("как много чисел вы хотите внести в список: "))
some_list=[]
counter=0
while counter<how_many:
    print(f"Введите {counter+1} элемент списка")
    user_input=float(input(">>>>>"))
    some_list.append(user_input)
    counter+=1
print(f"Изначальный список- {some_list}")
some_list=[int(i) for i in some_list]
print(f"После преобразования- {some_list}")