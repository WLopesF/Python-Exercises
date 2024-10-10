nota1 = float (input("Digite a primeira nota"))
nota2 = float (input("Digite a segunda nota"))
nota3 = float (input("Digite a terceira nota"))

average = (nota1 + nota2 + nota3)/3

if (average == 10) :
   print ("Parabéns. Você é nota 10!")

if (average == 8 and 9) :
   print("Parabéns! Você está mais que aprovado.")

if (average == 7) :
   print("Muito bem! Você foi aprovado")

if (average < 7) :
   print("Que pena... Você foi reprovado. Estude um pouco mais da próxima vez")
