string1 = input("Digite o seu primeiro nome: ")
string2 = input("Digite o seu sobrenome: ")
string3 = int(input("Digite a sua idade: "))
string4 = input("Você é estudante?")
                
if string4 in["Sim", "Sou"]:
   string5 = input("Em qual ano ou área?")
if (string5):
   string6 = input("Em qual escola ou universidade?")
   print("Olá, o seu nome é", string1, "seu sobrenome é", string2, "e você tem", string3, "anos de idade. Você é estudante do", string5, "na", string6, ".")
else:
   print("Olá, o seu nome é", string1, "seu sobrenome é", string2, "e você tem", string3, "anos de idade e você não é estudante. Nunca é tarde demais pra aprender!")
         
