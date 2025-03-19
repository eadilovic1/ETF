import z3

x = z3.Bool('x')
y = z3.Bool('y')
z = z3.Bool('z')

k1 = z3.Xor(x, z3.Implies(y, z))
k2 = z3.Implies(z3.Not(y), x)
k3 = z3.Implies(y, z3.And(x, z))

s = z3.Solver()

s.add(k1)
s.add(k2)
s.add(k3)

provjera = s.check()
print("Provjera: ", provjera)

# pokušaj pronalaska modela za kojeg je izraz zadovoljavajući
try:
    model = s.model()
    print("Model: ", model)
except:
    print("Greška prilikom dohvatanja modela!")

# sada imamo tri literala pa nam je potrebno samo 2^3 = 8 binarnih brojeva
# ove brojeve sada zapisujemo na tri bita
binarni = ['000', '001', '010', '011', '100', '101', '110', '111',]

print("TABLICA ISTINE:")
print()
print("---------------------------------")
print("|   x   |   y   |   z   | IZRAZ |")
print("---------------------------------")

for i in range (8):
    X = bool(int(binarni[i][0]))
    Y = bool(int(binarni[i][1]))
    Z = bool(int(binarni[i][2]))

    k1 = z3.Xor(X, z3.Implies(Y, Z))
    k2 = z3.Implies(z3.Not(Y), X)
    k3 = z3.Implies(Y, z3.And(X, Z))

    s1 = z3.Solver()
    s1.add(k1)
    s1.add(k2)
    s1.add(k3)

    print("|", "{:<5}".format(X), "|", "{:<5}".format(Y), "|", "{:<5}".format(Z), "|", end = " ")
    if s1.check() == z3.sat:
        print("  1   |")
    else:
        print("  0   |")
    print("---------------------------------")
