def fizzbuzz(n: int):
  if isinstance(n, str):
    return None

  res = ''

  if n % 3 == 0:
    res += 'fizz'

  if n % 5 == 0:
    res += 'buzz'

  if res == '':  
    return n

  return res
