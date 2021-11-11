def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

def agrupe_melhor(seq, n):
  iters = [ iter(seq) ] * n
  return zip(*iters)

#assert list(better_grouper(range(100), 2)) == list(agrupe_melhor(range(100), 2))

#for _ in better_grouper(range(10**7), 10):
#    pass

for _ in agrupe_melhor(range(10**7), 10):
    pass
