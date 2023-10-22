a,b = 1,2
n = int(input("Enter the number of terms: "))
print(a)
print(b)

for _ in range(n-2):
	next_term = a+b
	print(next_term)
	a,b = b, next_term