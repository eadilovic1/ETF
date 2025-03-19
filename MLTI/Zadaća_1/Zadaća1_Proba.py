# uvođenje z3 biblioteke z3
import z3

# deklarisanje dviju bool varijabli x i y
x = z3.Bool("x")
y = z3.Bool("y")

# z3 biblioteka nam daje konstruktore za disjunkciju, konjunkciju, negaciju, implikaciju i ekskluzivnu disjunkciju
# ekvivalencija implementira pomoću operatora ==

# kreiranje bool formula(klauza) pomoću ranije deklarisanih bool varijabli x i y
x_or_y = z3.Or([x,y]) # disjunkcija
x_and_y = z3.And([x,y]) # konjunkcija
not_x = z3.Not(x) # negacija
x_or_y_if_not_x = (x_and_y == not_x) # formula (x_and_y <=> not_x) a ne boolean vrijednost

# kreirane klauze potrebno je dalje proslijediti solveru
s = z3.Solver() # kreiranje solvera s
s.add(x_or_y) # dodavanje klauze: x or y
z = z3.Bool("z")
s.add(z3.Or([x, y, z3.Not(z)])) # dodavanje još jedne klauze: x or y or !z

# pozivom s.check() ispitujemo da li kreirani solver sa na izlazu daje sat ili unsat
# s.check() vraća sat or unsat za formulu kreiranu konjunkcijom klauza koje smo proslijedili solveru pozivom s.add()
provjera = s.check()
print("Provjera: ", provjera)

# ako s.check() vraća sat, možemo pronaći odgovarajući model ulaza za taj slučaj koristeći s.model()
print("Model: ", s.model())






