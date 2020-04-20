
list_values = ['asasas|sadsds|', 'dqwdqawd | sasas ', 'sdasasa|saass'] 
print(list_values)

new_list = []

for e in list_values:
    g = [i for i, n in enumerate(e) if n == '|']      
    if len(g) == 2:
        change_list= list(e)
        change_list[g[1]] = 'x'
        change_string = ''.join(change_list)
        new_list.append(change_string)
    else:
        new_list.append(e)


print(new_list)