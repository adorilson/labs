def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

def agrupe(seq, n):
    num_grupos = len(seq) // n
    grupos = []
    for i in range(num_grupos):
        um_grupo = tuple(seq[i*n:(i+1)*n])
        grupos.append(um_grupo)

    return grupos

#assert naive_grouper(range(100), 2) == agrupe(range(100), 2)

for _ in agrupe(range(10**7), 10):
    pass

