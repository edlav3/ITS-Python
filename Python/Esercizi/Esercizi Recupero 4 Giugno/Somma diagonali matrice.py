def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    somma_D=0
    i=0
    while i<len(matrix):
        somma_D+=matrix[i][i]
        i+=1
    return somma_D


def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    somma_d=0
    i=0
    lenght=len(matrix)-1
    while i<len((matrix)):
        somma_d+=matrix[i][lenght]
        lenght-=1
        i+=1
    return somma_d

matrice=[[1,3,8],
         [1,9,3],
         [2,3,4]]

print(sum_primary_diagonal(matrice))
print(sum_secondary_diagonal(matrice))