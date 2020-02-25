




ref_list = []
def read_ref():
    with open('input.csv', 'r') as file:
        for line in file:
            ref_list.append(line.strip('\n'))
    return ref_list

ref_list = read_ref()
for i in ref_list:
    print(i)
