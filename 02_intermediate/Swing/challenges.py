lst = [ 99, 'no data', 95, 94, 'no data']

def only_numbers(lst):
    new_lst = [i if type(i) != str else 0 for i in lst ]
    return new_lst

def positive(lst):
    new_lst = [i for i in lst if i > 0]
    return new_lst

def string_sum(lst):
    new_lst = [float(i) for i in lst]
    total = sum(new_lst)
    return total

print(only_numbers(lst))


# new_temps = [temp / 10 for temp in temps if temp > 0]
# temps = [221, 234, 340, -9999, 230]
# new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
# print(new_temps)