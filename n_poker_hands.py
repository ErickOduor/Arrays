# Bonus: Compose a program that takes an integer command-line argument n and n poker hands (five cards each) from a sheffled deck, seperated by blank lines
import random

print('S = spade, H = heart, C = Cloves, D = Diamonds')
print('J = Jack, Q = Queen, K = King')
print('One = 1, Two = 2, Thr = 3, Fou = 4, Fiv = 5, Six =6, Sev =7, Eig = 8, Nin = 9, Ten =10')
card_deck = ['One_S','Two_S','Thr_S','Fou_S','Fiv_S','Six_S','Sev_S','Eig_S','Nin_S','Ten_S','JS','QS','KS','One_H','Two_H','Thr_H','Fou_H','Fiv_H','Six_H','Sev_H','Eig_H','Nin_H','Ten_H','JH','QH','KH','One_C','Two_C','Thr_C','Fou_C','Fiv_C','Six_C','Sev_C','Eig_C','Nin_C','Ten_C','JC','QC','KC','One_D','Two_D','Thr_D','Fou_D','Fiv_D','Six_D','Sev_D','Eig_D','Nin_D','Ten_D','JD','QD','KD']

n = int(input('Enter the number number of poker hands you you need: '))
a = []
b = []
if n < 10:
    for i in range(1, n):
        a.append(random.choices(card_deck, k=5))
        if a in b:
            break
        else:
            b.extend(a)
        
print(b)




