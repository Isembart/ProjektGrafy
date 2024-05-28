A = [
    [0, 1, 1, 0,1],
    [1, 0, 1, 6,0],
    [1, 1, 0, 5,0],
    [0, 0, 3, 0,0],
    [1, 0, 0, 0,0]
]

class WarshallReturn:
    def __init__(self, Distance, PreviousNode):
        self.Distance = Distance
        self.PreviousNode = PreviousNode

# funkcja do wyświetlania macierzy
def printMatrix(A):
    print("  ", end=' ')
    for i in range(len(A)):
        print(f'{i:5d}', end=' ')
    print()
    print("  _______________________________")
    for i in range(len(A)):
        print(f'{i}|', end=' ')
        for j in range(len(A)):
            print(f'{A[i][j]:5d}', end=' ')
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
    return WarshallReturn(Distance, PreviousNode)


print("Macierz sasiedztwa: ")
printMatrix(A)
Result = test(A)

start = input("Podaj indeks wierzcholka startowego: ")
end = input("Podaj indeks wierzcholka koncowego: ")

print(f"Odleglosc od {start} do {end} wynosi: {Result.Distance[int(start)][int(end)]}")
print(f"Sciezka: {end}", end=' ')
while(int(start) != int(end)):
    end = Result.PreviousNode[int(start)][int(end)]
    print(f"<- {end} ", end='')
print()


