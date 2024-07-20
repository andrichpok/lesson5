immutable_var = (1, 2, 'phone', True)
print(immutable_var)
 # immutable_var[0] = 27 # данные кортежа изменить нельзя

mutable_list = ['black', 'green', 'white', 5, False]
mutable_list[2] = 'yellow'
mutable_list[3] = 8
mutable_list.append('ghost')
mutable_list.extend([123])
print(mutable_list)
