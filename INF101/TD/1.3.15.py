'''
Author: JIANG Yilun
Date: 2021-10-02 15:56:57
LastEditTime: 2021-10-06 10:03:45
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TD/1.3.15.py
'''
A = int(input("Entrer: "))

n = 1
Un = A
Un_max = A
count_descente = 1
count_descente_max = 2
Un_prev = Un

while Un != 1:
    if Un % 2 == 0:
        Un = Un / 2
    else:
        Un = 3 * Un + 1
        print("La valeur dela suite au terme %i est egale a %i" % (n, Un))

    if Un > Un_max:
        Un_max = Un

    if Un < Un_prev:
        count_descente += 1
    else:
        count_descente = 1
    Un_prev = Un

    if count_descente > count_descente_max:
        count_descente_max = count_descente

    print("Un a l'etape %i est egale a %i" % (n, Un))
    n += 1

print("Un = 1 lorsque n eset egale a %i et la plus grand valeur atteint par la suite %i" % (n, Un_max))
