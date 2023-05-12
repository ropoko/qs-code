def factorial(n: int) -> int:
  if isinstance(n, str):
    return None

  if n == 1 or n == 0:
    return n
  else:
    return n * factorial(n - 1)
