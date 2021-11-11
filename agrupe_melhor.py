def agrupe_listas(l1, l2):
  return zip(iter(l1), iter(l2))

# x = agrupe_listas([1]*10*8, [2]*10**8)
for _ in agrupe_listas([1]*10*10, [2]*10**10):
    pass
