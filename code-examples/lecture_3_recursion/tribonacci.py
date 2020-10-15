def tribonacci(n):
  if n<2:
    return 1
  return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

for i in range(20):
  print(str(i)+ ";"+ str(tribonacci(i))) 