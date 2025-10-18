euro = float(input("Quanto deseja converter: "))
print()
print("""Qual moeda deseja converter:
[o] Real Brasileiro
[1] Baht Tailandês
[2] Surce Equador""")
moeda=int(input("Escolha sua opção: "))
real=5.32*euro
baht=31.10*euro
surce=29700*euro
print()
if moeda==0:
    print("Isso lhe dará", real, "Reais Brasileiros")
elif moeda==1:
    print("Isso lhe dará", baht, "em Baht Tailandeses")
else:
    print("Isso lhe dará", surce, "em Surces do Equador")
