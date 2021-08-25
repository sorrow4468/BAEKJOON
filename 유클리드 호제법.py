import timeit
start = timeit.default_timer()


a, b = 12368711, 2678178

while a % b != 0:
    a, b = b, a % b

print(b)




# for i in range(max(a,b),0,-1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

end = timeit.default_timer()
print(f'{end-start:.5f}')