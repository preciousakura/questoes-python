def mediaTurma(notas):
  media = 0.0
  for i in notas:
    media = media + float(i['media'])
  return media/(len(notas))
  
def ordenar(notas):
  return sorted(notas, key=lambda k:k['media'], reverse=True)

arquivo = open("questao2.txt", "r")
notas = []
erros = []

for linha in arquivo.readlines():
  aluno = {}
  alunoInfos = linha.split(":")
  if(len(alunoInfos) != 5):
    erros.append(alunoInfos)
  else:
    aluno["matricula"] = alunoInfos[0]
    aluno["nome"] = alunoInfos[1]
    aluno["nota1"] = alunoInfos[2]
    aluno["nota2"] = alunoInfos[3]
    aluno["nota3"] = alunoInfos[4]
    aluno["media"] = (float(alunoInfos[2]) + float(alunoInfos[3]) + float(alunoInfos[4]))/3
    notas.append(aluno)

notas_ordenadas = ordenar(notas)

for i in range(len(notas_ordenadas)):
  nome = notas_ordenadas[i]["matricula"]+".txt"
  gravar = open(nome, "w")
  gravar.write("Universidade Federal do Ceará\n")
  gravar.write("Disciplina de Introdução à Computação\n")
  gravar.write("Aluno(a): "+notas_ordenadas[i]["nome"].upper()+" "+"("+ notas_ordenadas[i]["matricula"]+")\n\n")
  
  gravar.write(f"Nota de Cálculo 1: {float(notas_ordenadas[i]['nota1']): .2f}\n")
  gravar.write(f"Nota de Língua Portuguesa: {float(notas_ordenadas[i]['nota2']): .2f}\n")
  gravar.write(f"Nota de Metodologia Científica: {float(notas_ordenadas[i]['nota3']): .2f}\n\n")
  
  gravar.write(f"Média do Aluno: {float(notas_ordenadas[i]['media']): .2f}\n")
  gravar.write(f"Média da Turma: {mediaTurma(notas_ordenadas): .2f}\n")
  gravar.write("Posição na Turma: "+str(i+1)+"/"+str(len(notas_ordenadas)))

  gravar.close()
  

gravar = open("erros.txt", "w")
gravar.write("Universidade Federal do Ceará\n")
gravar.write("Disciplina de Introdução à Computação\n")
gravar.write("Alunos com falta de informações\n\n")

for i in range(len(erros)):
  gravar.write(str(i+1)+" - "+erros[i][1].upper()+"\n")
  
gravar.write("\nTotal: "+str(len(erros))+" alunos")
gravar.close()

  

  