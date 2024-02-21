S = 144
S0 = int(input())
T0 = int(input())
T = 100

#公式
ans1 = (S - S0) / S 
ans2 = (ans1)**(T/T0)
ans3 = 1 - ans2
finile = S * ans3

print(finile)

