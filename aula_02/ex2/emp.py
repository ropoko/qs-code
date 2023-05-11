class Empregado:
  taxa_reajuste = 1.05

  cargos_validos = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']

  def __init__(self, nome: str, sobrenome: str, cargo: str, salario: int):
    self.nome = nome
    self.sobrenome = sobrenome
    self.cargo = cargo.lower()
    self.salario = salario

  def calcular_reajuste(self) -> int:
    novo_salario = self.salario + (self.salario * self.taxa_reajuste)

    return novo_salario

  def gerar_nome_completo(self) -> str:
    return f'{self.nome} {self.sobrenome}'

  def validar_cargo(self) -> bool:
    if self.cargo in self.cargos_validos:
      return True
    else:
      return False
