# https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/chaves/

num_lines = int(input())
num_brackets = 0

fail = False

for i in range(num_lines):
    line_input = list(input())
    for char in line_input:
        if char == '{' :
            num_brackets += 1
        elif char == '}':
            num_brackets -= 1
        if num_brackets < 0:
            fail = True
            break

if num_brackets == 0 and fail == False:
    print('S')
if num_brackets != 0 or fail == True:
    print('N')
