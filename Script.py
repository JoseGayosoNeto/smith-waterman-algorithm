def inicializar_matriz(seqV, seqH, match, mismatch, gap):
    m = len(seqH)
    n = len(seqV)
    matriz = [[]] * (n + 2)
    for i in range(len(matriz)):
        matriz[i] = [0] * (m + 2)
    matriz[n][0], matriz[n+1][0], matriz[n+1][1] = 'U', 'X', 'U'
    for i in range(len(seqV)):
        matriz[i][0] = seqV[n-1-i]
    for j in range(len(seqH)):
        matriz[-1][j+2] = seqH[j]

    for i in range(len(seqV)):
        matriz[i][1] = (n-i) * gap
    for j in range(len(seqH)):
        matriz[-2][j+2] = (j+1) * gap

    for i in range(n):
        for j in range(m):
            if matriz[-3-i][0] == matriz[-1][j+2]:
                mis_or_match = match
            else:
                mis_or_match = mismatch

            mis_or_match = matriz[-2-i][j+1] + mis_or_match    
            gap_left = matriz[-3-i][j+1] + gap
            gap_down = matriz[-2-i][j+2] + gap
            
            matriz[-3-i][j+2] = max(gap_left, gap_down, mis_or_match)

    return matriz

def print_output(matriz, match, mismatch, gap, score, alin_V, alin_H):
    
    print('--------------------------------------------------------------------------------')
    print('** valores de score **')
    print('================================================================================')
    for linha in matriz:
        print(linha)
    print('================================================================================')
    print('--------------------------------------------------------------------------------')
    print(f'Alinhamento ** score = {score} ** Match = {match} | Mismatch = {mismatch} | Gap = {gap}')
    print('--------------------------------------------------------------------------------')
    print(f'{alin_V}')
    print(f'{alin_H}')
    print('--------------------------------------------------------------------------------')


def backtracing(matriz, seqV, seqH, match, mismatch, gap):
    i, j = len(seqV)-1, len(seqH)-1
    alin_V, alin_H = str(), str()
    score = matriz[-3-i][j+2]
    while i >= 0 and j >= 0:
        if matriz[-3-i][0] == matriz[-1][j+2] and matriz[-3-i][j+2] == matriz[-2-i][j+1] + match:
            alin_V = matriz[-3-i][0] + alin_V
            alin_H = matriz[-1][j+2] + alin_H
            i -= 1
            j -= 1
        elif matriz[-3-i][j+2] == matriz[-2-i][j+1] + mismatch:
            alin_V = matriz[-3-i][0] + alin_V
            alin_H = matriz[-1][j+2] + alin_H
            i -= 1
            j -= 1
        elif matriz[-3-i][j+2] == matriz[-2-i][j+2] + gap:
            alin_V = matriz[-3-i][0] + alin_V
            alin_H = "-" + alin_H
            i -= 1
        else:
            alin_V = "-" + alin_V
            alin_H = matriz[-1][j+2] + alin_H
            j -= 1
    while i >= 0:
        alin_V = matriz[-3-i][0] + alin_V
        alin_H = "-" + alin_H
        i -= 1
    while j >= 0:
        alin_V = "-" + alin_V
        alin_H = matriz[-1][j+2] + alin_H
        j -= 1
    
    
    
    return alin_V, alin_H, score

def ler_arquivo(filename):
    
    with open(filename, 'r') as arq:
        linhas = arq.readlines()
        seq1 = linhas[0].strip()
        seq2 = linhas[1].strip()
        gap = int(linhas[2].strip())
        mismatch = int(linhas[3].strip())
        match = int(linhas[4].strip())
        
        return seq1, seq2, gap, mismatch, match

if __name__ == "__main__":
    seqV, seqH, gap, mismatch, match = ler_arquivo('input.txt')
    matriz = inicializar_matriz(seqV, seqH, match, mismatch, gap)
    alin_V, alin_H, score = backtracing(matriz, seqV, seqH, match, mismatch, gap)
    print_output(matriz, match, mismatch, gap, score, alin_V, alin_H)