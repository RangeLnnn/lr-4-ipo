how_many=int(input("как много чисел вы хотите внести в список: "))
some_list=[]
counter=0
while counter<how_many:
    print(f"Введите {counter+1} элемент списка")
    user_input=float(input(">>>>>"))
    some_list.append(user_input)
    counter+=1
counter=0
for i in some_list:
    if i>10:
        counter+=1
print("В вашем списке ",counter," чисел больше чем 10")
