try:
  while True:
    monica = int(input())
    filho_um = int(input())
    filho_dois = int(input())

    filho_tres = monica - (filho_um+filho_dois)

    mais_velho = max(filho_um, filho_dois, filho_tres)

    print(mais_velho)
except:
  pass
