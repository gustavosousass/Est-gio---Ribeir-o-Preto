# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):

  fib_sequence = [0, 1]

  while True:
      next_value = fib_sequence[-1] + fib_sequence[-2]
      if next_value > n:
          break
      fib_sequence.append(next_value)

  return fib_sequence

def pertence_a_fibonacci(num):
  fib_sequence = fibonacci(num)
  return num in fib_sequence

try:
  numero = int(input("Informe um número: "))
  if pertence_a_fibonacci(numero):
      print(f"O número {numero} pertence à sequência de Fibonacci.")
  else:
      print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
  print("Por favor, insira um número inteiro válido.")

#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_letra_a(texto):

  texto_minusculo = texto.lower()

  
  quantidade_a = texto_minusculo.count('a')


  existe_a = quantidade_a > 0

  return existe_a, quantidade_a

texto_usuario = input("Digite uma string: ")

existe, quantidade = contar_letra_a(texto_usuario)

if existe:
  print(f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade} vez(es) na string.")
else:
  print("A letra 'a' não está presente na string.")

#4) Descubra a lógica e complete o próximo elemento:
# A)1, 3, 5, 7, ___
#Lógica: Nimpares consecutivos.
#Próximo termo:9

#b) 2, 4, 8, 16, 32, 64, ____
#Lógica: Cadadobro do anterior.
#64x2=128

#1, 1, 2, 3, 5, 8, ____
#Lógica: **Sequência de Fibonacci:
#Próximo termo:(5
#5+8=13

#Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  


#Primeiro passo: Trabalhe com os interruptores.

#Chame os interruptores de A, B e C.
#Ligue ou troque Ae **deixe ligado por um tempo(
#Após esse tempo, desligue o interruptor A.
#Ligue ou interruptor Bedeixe-o ligado .
#O interruptor C permanece desligadoo
#Primeira ida: Vá até a sala das lâmpadas.

#Ao entrar nas salas das lâmpadas, você observará:
#Uma lâmpada acesa:interruptor B(
#Uma lâmpada apagada, mas quente:interruptor A(
#Uma lâmpada apagada e fria : Essa lâmpadainterruptor C(
#Segunda ida:Não


#gustavo sousa da costa

