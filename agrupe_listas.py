def agrupe_listas(l1, l2):
  grupos = []
  for i, e in enumerate(l1):
    um_grupo = (e, l2[i])
    grupos.append(um_grupo)

  return grupos

# x = agrupe_listas([1]*10*8, [2]*10**8)
for _ in agrupe_listas([1]*10*10, [2]*10**10):
    pass
