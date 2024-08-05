my_dict = {'Ivan': 1992, 'Mama': 1951, 'Yar': 1993, 'Anton': 1991}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Iren'))
my_dict.update({'Irina': 1991,
               'Artem': 2001})
A = my_dict.pop('Anton')
print(A)
print(my_dict)
my_set = {1, 33, True, 'Anton', 1, 33, True, 'Anton', 1, (1,2,3,4)}
print(my_set)
my_set.update([7, 'Skaz'])
my_set.remove(1)
print(my_set)