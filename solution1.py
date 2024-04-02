def count_down(n):

  if n==0:
    return 0
  
  print(n)
  count_down(n-1)

n=4
  
count_down(n)