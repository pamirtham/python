l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))

for n in range(l,u + 1):
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if n == sum:
       print(num)
