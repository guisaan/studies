# > Operadores Booleanos

"""
< > : menor/maior que
<= => : menor/maior ou igual a que
== : comparado/igual a
!= : diferente de

Não há necessidade lógica de comparação numérica entre variáveis str, apenas igualdades ou diferenças textuais,
Apenas variáveis compostas por dados numéricos terão resultados lógicos.
"""

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2)				# false
print(idade1 <= idade2)			# true
print('Python' == 'python')		# false
print('banana' != 'abacaxi')		# true
print(altura1 >= altura2)			# true
print(altura2 > altura3)			# false