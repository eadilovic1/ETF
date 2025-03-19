import z3

a = z3.Bool('a')
b = z3.Bool('b')
c = z3.Bool('c')
d = z3.Bool('d')

k1 = z3.Implies(z3.Or(a, z3.Not(b)), z3.Xor(c, z3.Not(d)))
k2 = (c == z3.And(a, b))
k3 = z3.Implies(z3.Not(b), z3.Xor(z3.Not(a), z3.Not(c)))
k4 = z3.Implies(d, (z3.And(z3.Not(b), c)))

s = z3.Solver()

s.add(k1)
s.add(k2)
s.add(k3)
s.add(k4)

provjera = s.check()
print("Provjera: ", provjera)
# pronalaženje i ispisivanje modela za koje je kreirana formula tačna
while s.check() == z3.sat:
    model = s.model()
    print("Model:", model)
    lista = []
    for var in model:
        c = var()
        lista.append(c != model[var])
    s.add(z3.Or(lista))

binarni = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', 
           '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

print("TABLICA ISTINE:")
print()
print("-----------------------------------------")
print("|   a   |   b   |   c   |   d   | IZRAZ |")
print("-----------------------------------------")

for i in range (16):
    A = bool(int(binarni[i][0]))
    B = bool(int(binarni[i][1]))
    C = bool(int(binarni[i][2]))
    D = bool(int(binarni[i][3]))

    k1 = z3.Implies(z3.Or(A, z3.Not(B)), z3.Xor(C, z3.Not(D)))
    k2 = (C == z3.And(A, B))
    k3 = z3.Implies(z3.Not(B), z3.Xor(z3.Not(A), z3.Not(C)))
    k4 = z3.Implies(D, z3.And(z3.Not(B), C))

    s1 = z3.Solver()
    s1.add(k1)
    s1.add(k2)
    s1.add(k3)
    s1.add(k4)

    print("|", "{:<5}".format(A), "|", "{:<5}".format(B), "|", "{:<5}".format(C), 
          "|", "{:<5}".format(D), "|", end = " ")
    if s1.check() == z3.sat:
        print("  1   |")
    else:
        print("  0   |")
    print("-----------------------------------------")
