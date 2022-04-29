def comp(s1, s2):
    k = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            k += 1
    return k == 1


def check_perm(line):
    for i in range(len(line)-1):
        if not(comp(line[i], line[i+1])):
            return False
    return True


def perm(line):
    for i in range(5):
        new_line = [''] * 5
        new_line[0] = line[i]
        for j in range(5):
            if j == i:
                continue
            new_line[1] = line[j]
            for k in range(5):
                if k == i or k == j:
                    continue
                new_line[2] = line[k]
                for l in range(5):
                    if l == i or l == j or l == k:
                        continue
                    new_line[3] = line[l]
                    for m in range(5):
                        if m == i or m == j or m == k or m == l:
                            continue
                        new_line[4] = line[m]

                        if check_perm(new_line):
                            print("Answer")
                            print(line)
                            print(new_line)
                            return


lines = [
            ['0000', '1010', '1001', '1101', '0111'],
            ['0000', '1010', '1110', '0101', '1011'],
            ['1001', '1010', '1011', '0011', '0111'],
            ['0000', '0100', '1100', '0010', '1011'],
            ['1010', '0110', '1001', '0101', '1101'],
            ['0010', '1010', '0101', '0011', '0111'],
            ['1000', '1100', '0010', '0110', '0101'],
            ['1000', '0100', '1110', '0001', '0111']
         ]

for line in lines:
    perm(line)


#Вариант со встроенной перестановкой


import itertools


for line in lines:
    permutations_of_line = list(itertools.permutations(line))       #возвращает список всех возможных перестановок
    for permutation in permutations_of_line:
        if check_perm(permutation):
            print("Answer")
            print(line)
            break
