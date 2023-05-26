# Write a for loop inside of a list

# SIMPLE

x = [i for i in range(10)]

print(x)


# Little more advanced
y = [[j for j in range(5)] for i in range(10)]

print(y)


# Even better

z = [i for i in range(10) if i % 2 == 0]
print(z)