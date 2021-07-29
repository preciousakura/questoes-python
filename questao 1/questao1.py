def verifica(palavra, hastags):
    for linha in hastags:
        if linha.lower() in palavra.lower():
            return False
    return True

arq_hastag = open("hashtags.txt", "r") 

frequencia = []
hastags_sem_repeticao = []
hastags = []

for linha in arq_hastag.readlines():
  palavra = linha.split("\n")[0]
  if (verifica(palavra, hastags_sem_repeticao)):
    hastags_sem_repeticao.append(linha.split("\n")[0])
  hastags.append(palavra)
    
    
for palavra in hastags_sem_repeticao:
  word = {}
  word["palavra"] = palavra
  qtd = 0
  for hastag in hastags:
    if(hastag == palavra):
      qtd += 1
  word["frequencia"] = qtd
  frequencia.append(word)
  
frequencia =  sorted(frequencia, key=lambda k: k['frequencia'], reverse=True)

print("Hastag mais popular:", frequencia[0]['palavra']+",","frequência: ", frequencia[0]['frequencia'])
print("Hastag menos popular:", frequencia[len(frequencia)-1]['palavra']+",","frequência: ", frequencia[len(frequencia)-1]['frequencia'])
    

  