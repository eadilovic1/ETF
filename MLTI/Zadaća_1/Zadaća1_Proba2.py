from pysat.solvers import Glucose3

# Kreiranje instanci SAT solvera
solver = Glucose3()

# Definisanje klauzula
clauses = [[1, 2, -3], [-1, 2, 3], [1, -2, -3], [-1, -2, 3]]

# Dodavanje klauzula u solver
for clause in clauses:
    solver.add_clause(clause)

# Rešavanje problema
if solver.solve():
    print("Rešenje pronađeno:")
    print(solver.get_model())  # Ispis rešenja
else:
    print("Nije moguće pronaći rešenje.")



import z3

#kon = z3.Bool('kon')

#kon = z3.And(a == True, b == True, c == True, d == True)
kon = z3.And(True, True, True, False)
kon = z3.And(bool(1), bool(1), bool(1), bool(0))

bool_vrijednost = z3.simplify(kon)

s1 = z3.Solver()
s1.add(kon)

if s1.check() == z3.sat:
    print("KONJUNKCIJA: True")
else:
    print("KONJUNKCIJA: False")

#print("KONJUNKCIJA: ", bool_vrijednost)

#kon = a and b and c and d
#kon = k1 and k2 and k3 and k4
#print("SKNF: ", kon)

#print(bool(0))