# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
string1 = "パトカー"
string2 = "タクシー"
string3 = ""
for i in range(len(string1)):
    string3+=string1[i:i+1:1]
    string3+=string2[i:i+1:1]
    i+=1
print(string3)