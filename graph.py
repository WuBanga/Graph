import numpy
lenght = int(input())

arcWeightMatrix = numpy.array([[0, 1, 0, 0, 0, 0, 1],
							   [1, 0, 1, 0, 0, 1, 0],
							   [0, 0, 0, 1, 1, 0, 1],
							   [0, 0, 0, 0, 1, 1, 1],
							   [0, 0, 0, 0, 0, 0, 0],
							   [0, 0, 0, 0, 1, 0, 0],
							   [0, 0, 0, 0, 0, 1, 0]
							  ])

lenMatrix = len(arcWeightMatrix)
graph = {}

for i in range(0 , lenMatrix):
	mass = []
	for j in range(0, lenMatrix):
		if arcWeightMatrix[i][j] != 0:
			mass.append(j + 1)
	graph[i + 1] = mass

def search(lenght):
	for i in range(0, lenMatrix):
		searchRecursion([i], arcWeightMatrix, lenght)

def searchRecursion(curPath, arcWeightMatrix, lenght):
	if len(curPath) == lenght:
		for i in range(0, len(curPath)):
			curPath[i] += 1
		print(curPath)
	else:
		lastElem = curPath[len(curPath) - 1]
		for j in range(0, lenMatrix):
			if not(j in curPath):
				if arcWeightMatrix[lastElem][j] != 0:
					newPath = curPath.copy()
					newPath.append(j)
					searchRecursion(newPath,  arcWeightMatrix, lenght)
						
search(lenght)
print(graph)