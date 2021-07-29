esportes = []
paises = []
provas = []

olimpiadas_medalhas = []

arq_esporte = open("esportes.txt", "r")
arq_paises = open("paises.txt", "r")
arq_provas = open("provas.txt", "r")

for linha in arq_provas.readlines():
  prova = {}
  provaInfo = linha.split(":")
  prova["codigo"] = provaInfo[0]
  prova["categoria"] = provaInfo[1]
  prova["ouro"] = provaInfo[2].split("\n")[0]
  prova["prata"] = provaInfo[3].split("\n")[0]
  prova["bronze"] = provaInfo[4].split("\n")[0]
  provas.append(prova)
arq_provas.close()

for linha in arq_paises.readlines():
  pais = {}
  paisInfo = linha.split("; ")
  pais["codigo"] = paisInfo[0]
  pais["pais"] = paisInfo[1].split("\n")[0]
  paises.append(pais)
arq_paises.close()

for linha in arq_esporte.readlines():
  esporte = {}
  esporteInfo = linha.split("; ")
  esporte["codigo"] = esporteInfo[0]
  esporte["esporte"] = esporteInfo[1].split("\n")[0]
  esportes.append(esporte)
arq_esporte.close()


for p in paises:
  medalha = {}
  medalha["pais"] = p["pais"]
  ouro = 0
  prata = 0
  bronze = 0
  for pro in provas:
    if(pro["ouro"] == p["codigo"]):
      ouro += 1
    if(pro["prata"] == p["codigo"]):
      prata += 1
    if(pro["bronze"] == p["codigo"]):
      bronze += 1
  medalha["ouro"] = ouro
  medalha["prata"] = prata
  medalha["bronze"] = bronze
  medalha["total"] = int(medalha["ouro"]) + int(medalha["prata"]) + int(medalha["bronze"])
  olimpiadas_medalhas.append(medalha)
  

  
olimpiadas_medalhas =  sorted(olimpiadas_medalhas,
                          key=lambda k: (k['ouro'], k['prata'], k['bronze']), reverse=True)

quadro_medalha = open("quadro_medalhas.txt", "w")
quadro_medalha.write("Olimpíadas 2020\n")
quadro_medalha.write("Quadro de Medalhas\n\n")
quadro_medalha.write(f'{"Pais":29} {"Ouro":10} {"Prata":10} {"Bronze":10} {"Total":10}\n')
quadro_medalha.write('-'*70+"\n")
for i in olimpiadas_medalhas:
  quadro_medalha.write(f'{i["pais"]:20} {i["ouro"]:10} {i["prata"]:10} {i["bronze"]:10} {i["total"]:10}\n')
quadro_medalha.close()


quadro_modalidade = open("quadro_modalidade.txt", "w")
quadro_modalidade.write("Olimpíadas 2020\n")
quadro_modalidade.write("Compeões por modalidade\n\n")

for es in esportes:
  modalidade = {}
  modalidade = es["esporte"]
  
  ouro = []
  prata = []
  bronze = []
  
  modalidades = []
  medalhas = {}
  
  cont = 0
  for pr in provas:
    if(pr["codigo"] == es["codigo"]):
      ouro.append(pr["ouro"])
      prata.append(pr["prata"])
      bronze.append(pr["bronze"])
      cont += 1
      
  if cont > 0:
    medalhas["modalidade"] = es["esporte"]
    medalhas["ouro"] = ouro
    medalhas["prata"] = prata
    medalhas["bronze"] = bronze
    modalidades.append(medalhas)
    
    for i in modalidades:
      quadro_modalidade.write("Modalidade: "+i['modalidade']+"\n")
      frequencia = []
      
      for country in paises:
        pais = {}
        pais["pais"] = country["pais"]

        ouro_p = 0 
        prata_p = 0 
        bronze_p = 0
        
        for o in i["ouro"]:
          if(o == country['codigo']): 
            ouro_p += 1
        for p in i['prata']:
          if(p == country['codigo']): 
            prata_p += 1
        for b in i['bronze']:
          if(b == country['codigo']): 
            bronze_p += 1
            
        pais["ouro"] = ouro_p
        pais["prata"] = prata_p
        pais["bronze"] = bronze_p
        pais["total"] = ouro_p + prata_p + bronze_p
        
        frequencia.append(pais)
        
      frequencia = sorted(frequencia, key=lambda k: (k['ouro'], k['prata'], k['bronze']), reverse=True)
      quadro_modalidade.write("Campeão: ")
  
      quadro_modalidade.write(frequencia[0]['pais'])    
      for mod in range(1, len(frequencia)):
        if(frequencia[0]['ouro'] == frequencia[mod]['ouro'] and frequencia[0]['prata'] == frequencia[mod]['prata'] and frequencia[0]['bronze'] == frequencia[mod]['bronze']):
          quadro_modalidade.write(" - "+frequencia[mod]['pais'])   
      
      quadro_modalidade.write(" ("+str(frequencia[0]['ouro'])+" Ouro - "+str(frequencia[0]['prata'])+" Prata - "+str(frequencia[0]['bronze'])+" Bronze)\n\n")
    
quadro_modalidade.close()