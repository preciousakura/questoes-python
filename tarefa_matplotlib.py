import numpy as np
import matplotlib.pyplot as plt
import time
np.set_printoptions(precision=3)



def insertionSort(arr):
	for i in range(1, len(arr)):
		key = np.copy(arr[i])
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = np.copy(arr[:mid])
		R = np.copy(arr[mid:])
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def partition(arr, low, high):
	i = (low-1)
	pivot = np.copy(arr[high])

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = np.copy(arr[j]), np.copy(arr[i])

	arr[i+1], arr[high] = np.copy(arr[high]), np.copy(arr[i+1])
	return (i+1)

def quickSort(arr, low=0, high=None):
	if high == None:
		high = len(arr)-1
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


y = np.array([500, 1000, 2000, 4000, 8000, 10000])
data = []

algoritmo = {}
algoritmo["nome"] = "mergeSort"
for i in y:
  ini = time.time()
  arr_1 = np.random.rand(i,1)*i
  mergeSort(arr_1)
  fim = time.time()
  algoritmo[str(i)+"valores"] = fim-ini
data.append(algoritmo)

ms = []
for i in y:
  ms.append(data[0][str(i)+"valores"])

fig = plt.figure(figsize=(6,6), dpi=80)

plt.ylabel("Tempo de Execução")
plt.xlabel("Número de Elementos")
plt.title(f'MergeSort')

plt.plot(y, ms)
plt.grid()
plt.show()

algoritmo = {}
algoritmo["nome"] = "quickSort"
for i in y:
  ini = time.time()
  arr_1 = np.random.rand(i,1)*i
  quickSort(arr_1)
  fim = time.time()
  algoritmo[str(i)+"valores"] = fim-ini
data.append(algoritmo)

qs = []
for i in y:
  qs.append(data[1][str(i)+"valores"])

fig = plt.figure(figsize=(6,6), dpi=80)


plt.ylabel("Tempo de Execução")
plt.xlabel("Número de Elementos")
plt.title(f'QuickSort')

plt.plot(y, qs)
plt.grid()
plt.show()

algoritmo = {}
algoritmo["nome"] = "insertionSort"
for i in y:
  ini = time.time()
  arr_1 = np.random.rand(i,1)*i
  insertionSort(arr_1)
  fim = time.time()
  algoritmo[str(i)+"valores"] = fim-ini
data.append(algoritmo)

isort = []
for i in y:
  isort.append(data[2][str(i)+"valores"])

fig = plt.figure(figsize=(6,6), dpi=80)

plt.ylabel("Tempo de Execução")
plt.xlabel("Número de Elementos")
plt.title(f'InsertionSort')

plt.plot(y, isort)
plt.grid()
plt.show()

x = np.array(["quickSort", "insertionSort", "mergeSort"])

for i in range(len(y)):
  valores = []
  valores.append(qs[i])
  valores.append(isort[i])
  valores.append(ms[i])

  fig = plt.figure(figsize=(6,6), dpi=80)



  plt.ylabel("Tempo de Execução")
  plt.title(f'Tempo de Execução por Algoritmo - {y[i]} valores')

  plt.bar(x, valores)
  plt.grid()
  plt.show()



