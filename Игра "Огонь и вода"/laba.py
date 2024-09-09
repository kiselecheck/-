sum = 0
n=int(input('Введите натуральное число:'))
for i in range(n+1):
    sum += ((-1)**i * (1/((2*i+1)*(4*i+1))))
    print(i, sum)
