'''
Знакомство с функциями.
Сумма кавдратов. Буквы из переданного аргументом текста. 
'''
def show(txt):
  symbs = list(set(txt))
  return symbs

def sqsum(n):
  nums = [k*k for k in range(1,n+1)]
  return(nums)
#тест
print(show("Mikhail Miroshnikov"))
print(sqsum(4))
