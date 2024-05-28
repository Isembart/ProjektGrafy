A = [
    [0, 1, 1, 0],
    [1, 0, 1, 6],
    [1, 1, 0, 5],
    [0, 0, 3, 0]
]

# funkcja do wyświetlania macierzy

def printMatrix(A):
    for i in range(len(A)):
        print(A[i], sep=' ')
    print()


# funkcja wykonująca algorytm floyda-warshalla 
# przyjmuje macierz na wejściu macierz sądziedztwa
# zwraca dwie macierze: pierwsza dlugość najkrótszej ścieżki z wierzchołki i (wiersz) do wierdzhołku j (kolumna)
# druga: zwraca poprzedni wierzchołek

def test(W):
    Distance = [[None for i in range(len(W))] for j in range(len(W))]
    PreviousNode = [[None for i in range(len(W))] for j in range(len(W))]
    # inicjalizacja
    for i in range(len(W)):
        for j in range(len(W)):
            if(i == j):
                Distance[i][j] = 0
                PreviousNode[i][j] = i
                continue
            if(W[i][j] == 0):
                Distance[i][j] = float('inf')
                PreviousNode[i][j] = None
                continue
            Distance[i][j] = W[i][j]
            PreviousNode[i][j] = i


    for i in range(len(W)):
        for j in range(len(W)):
            for v in range(len(W)):
                if(Distance[j][v] > Distance[j][i] + Distance[i][v]):
                    Distance[j][v] = Distance[j][i] + Distance[i][v]
                    PreviousNode[j][v] = PreviousNode[i][v]
    return (Distance, PreviousNode)


printMatrix(A)
printMatrix(test(A)[0])
printMatrix(test(A)[1])


