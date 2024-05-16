# smith-waterman-algorithm
Smith-Waterman algorithm made in Python

## COMO DEVE SER A ENTRADA:
arquivo texto com as duas sequencias. Uma sequencia em cada linha

Exemplo do arquivo de entrada, cujo nome DEVE SER input.txt:

Na linha 1 colocar a primeira sequencia (vertical)

Na linha 2 colocar a segunda sequencia (horizontal)

Na linha 3 colocar o valor de GAP

Na linha 4 colocar o valor de mismatch

Na linha 5 colocar o valor de match

Exemplo de arquivo:
```txt
ATCG
TCG
-2
-1
1
```

## COMO DEVE SER A SAIDA:

```
--------------------------------------------------------------------------------
** valores de score **
================================================================================
G -8 -5 -2 1 
C -6 -3 0 -2
T -4 -1 -2 -4
A -2 -1 -3 -5
U 0 -2 -4 -6
X U T C G
================================================================================
------------------------------------------------------------------
Alinhamento ** score = 1 ** Match = 1 | mismatch = -1 | Gap = -2
------------------------------------------------------------------
A T C G
- T C G
```