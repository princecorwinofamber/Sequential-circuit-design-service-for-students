import pyeda.inter

A, B, C, D = map(pyeda.inter.exprvar, "ABCD")

scheme = "~B & (A | (C | D))"
#            ^    ^    ^
#            |    |    Access is only allowed to staff with level 1 or higher
#            |    A supervisor may enter the laboratory regardless of
#            |    his/her access level
#            A dismissed employee can never enter the laboratory regardless of
#            his/her level of access or whether he/she is superior.

X = pyeda.inter.expr(scheme)

# BDD seems to fit better in this case
X = pyeda.inter.expr2bdd(X)
A, B, C, D = map(pyeda.inter.expr2bdd, [A, B, C, D])


INPUT_PROMPT = "Please, enter the values for A, B, C and D without spaces: "

#check that the input supplied by the user was right
def get_correct_input():
    while True:
        values = input(INPUT_PROMPT)
        if len(values) != 4 or not set(values).issubset({"0", "1"}):
            continue
        else:
            return map(int, values)

a_val, b_val, c_val, d_val = get_correct_input()
answer = X.restrict({A: a_val, B: b_val, C: c_val, D: d_val})
print("The answer is", bool(answer))
