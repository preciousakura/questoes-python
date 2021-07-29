def verifica(info, vetor):
    for dado in vetor:
        if dado in info:
            return False
    return True

dataset = []

autores = []
frequencia_autores = []

meses = []
frequencia_meses = []

palavras = []
frequencia_palavras = []

for i in range(2056):
  nome = "./dataset/post_"+str(i+1)+".txt"
  arq = open(nome, "r")

  text = arq.readlines()
  if(len(text) > 0):
    dados = {}
    dados["conteudo"] = text[0].split(": ")[1].split("\n")[0]
    dados["autor"] = text[1].split(": ")[1].split("\n")[0]
    dados["assunto"] = text[2].split(": ")[1].split("\n")[0]
    dados["publicado em"] = text[3].split(": ")[1].split("\n")[0]
    dataset.append(dados)

    
for i in dataset:
  if(verifica(i['autor'], autores)):
    autores.append(i['autor'])


for i in autores: 
  frequencia = {}
  qtd = 0
  for data in dataset:
    if i == data['autor']:
      qtd += 1
  frequencia["autor"] = i
  frequencia["frequencia"] = qtd
  frequencia_autores.append(frequencia)
  
  
for i in dataset:
  mes = i['publicado em'].split("/")[0]
  if(verifica(mes, meses)):
    meses.append(mes)

meses_nome = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in meses: 
  fr_mes = {}
  qtd = 0
  for data in dataset:
    mes = data['publicado em'].split("/")[0]
    if i == mes:
      qtd += 1
  fr_mes["mes"] = meses_nome[int(i)-1]
  fr_mes["frequencia"] = qtd
  frequencia_meses.append(fr_mes)
  
  
frequencia_meses =  sorted(frequencia_meses,
                          key=lambda k:k['frequencia'], reverse=True)
                          
frequencia_autores =  sorted(frequencia_autores,
                          key=lambda k:k['frequencia'], reverse=True)                        

print("Quantidade de publicações em cada mês:")
for i in frequencia_meses:
  print(i['mes']+":",i['frequencia'])
  
print("\nOS 3 meses com a maior quantidade de publicacões:")
for i in range(3):
  print(frequencia_meses[i]['mes']+":",frequencia_meses[i]['frequencia'])
  
print("\nOS 3 autores com a maior quantidade de publicacões:")
for i in range(3):
  print(frequencia_autores[i]['autor']+":",frequencia_autores[i]['frequencia'])
  
for i in dataset:
  word = i['conteudo'].split(" ")
  for p in word:
    if(len(p) > 5 and verifica(p, palavras)):
      palavras.append(p)

print("\nAs palavras com mais de 5 letras que mais aparecem nas publicações:")
print("Contabilizando, aguarde...")
for i in palavras: 
  fr_palavra = {}
  qtd = 0
  for data in dataset:
    word = data['conteudo'].split(" ")
    for p in word:
      if(len(p) > 5 and i == p):
        qtd += 1
        
  fr_palavra["palavra"] = i
  fr_palavra["frequencia"] = qtd
  frequencia_palavras.append(fr_palavra)
  
frequencia_palavras =  sorted(frequencia_palavras,
                          key=lambda k:k['frequencia'], reverse=True)   
                 
arq_palavras = open("frequencia_palavras.txt", "w")
for i in frequencia_palavras:
  arq_palavras.write("Palavra: "+i['palavra']+"\n")
  arq_palavras.write("Frequência: "+str(i['frequencia'])+"\n\n")
print("Savlo no arquivo frequencia_palavras.txt com sucesso!")

arq_autores = open("arquivo_autores.txt", "w")
arq_autores.write("AUTORES\n")
arq_autores.write("="*60+"\n\n")

for i in frequencia_autores:
  arq_autores.write(f"Nome: {i['autor']}\n")
  arq_autores.write(f"Publicações: {i['frequencia']}\n\n")
arq_autores.write("="*60)
    
    
    
