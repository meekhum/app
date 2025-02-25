N_pass=40
E_pass=45
M_pass=50
A_marks=51
B_marks=46
C_marks=33

print("PASSED NEPALI AND ENGLISH")
print("A")
print(N_pass<A_marks and E_pass<A_marks)
print("B")
print(N_pass<B_marks and E_pass<B_marks)
print("C")
print(N_pass<C_marks and E_pass<C_marks)
print("\n")

print("PASSED ALL SUBJECT")
print("A")
print(N_pass<A_marks and E_pass<A_marks and M_pass<A_marks)
print("B")
print(N_pass<B_marks and E_pass<B_marks and M_pass<B_marks)
print("C")
print(N_pass<C_marks and E_pass<C_marks and M_pass<C_marks)
print("\n")

print(True and True or False and False)
print(True or False and False)