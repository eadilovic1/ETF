# uvođenje biblioteke z3
import z3
# kreiranje literala
a = z3.Bool('a')
b = z3.Bool('b')
c = z3.Bool('c')
d = z3.Bool('d')
# kreiranje klauza
k1 = z3.Implies(a, z3.Or(z3.Not(b), z3.And(c, d)))
k2 = z3.And(a, d)
k3 = z3.Or(z3.Not(b), c)
# kreiranje traženog logičkog izraza
k = z3.Implies(z3.And(k1, k2), k3)
# kreiranje solvera i dodavanje kreiranog izraza u solver
s = z3.Solver()
s.add(k)
# provjera zadovoljivosti datog izraza
provjera = s.check()
print("PROVJERA: ", provjera)

# kreiranje liste prvih 2^4 = 16 binarnih brojeva zapisanih na 4 bita
# pomoću ove liste ćemo proći kroz sve moguće kombinacije ulaznih vrijednosti literala
binarni = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', 
           '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

print("TABLICA ISTINE:")
print()
print("-----------------------------------------")
print("|   a   |   b   |   c   |   d   | IZRAZ |")
print("-----------------------------------------")

for i in range (16):
    # kreiranje klasičnih bool varijabli 
    # na osnovu liste binarnih brojeva varijable poprimaju vrijednosti "True" ili "False"
    A = bool(int(binarni[i][0]))
    B = bool(int(binarni[i][1]))
    C = bool(int(binarni[i][2]))
    D = bool(int(binarni[i][3]))
    # kreiranje klauza za konkretne vrijednosti ulaznih varijabli
    k1 = z3.Implies(A, z3.Or(z3.Not(B), z3.And(C, D)))
    k2 = z3.And(A, D)
    k3 = z3.Or(z3.Not(B), C)
    # kreiranje logičkog izraza za konkretne vrijednosti ulaznih varijabli
    k = z3.Implies(z3.And(k1, k2), k3)
    # kreiranje solvera i dodavanje kreiranog izraza u solver
    s1 = z3.Solver()
    s1.add(k)
    # ispisivanje vrijednosti varijabli i samog izraza u tablicu istine
    print("|", "{:<5}".format(A), "|", "{:<5}".format(B), "|", "{:<5}".format(C), 
          "|", "{:<5}".format(D), "|", end = " ")
    if s1.check() == z3.sat:
        print("  1   |")
    else:
        print("  0   |")
    print("-----------------------------------------")
    