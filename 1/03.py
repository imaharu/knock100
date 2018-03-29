# 03. 円周率
pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
clear_pi = pi.replace(",", "").replace(".", "").split(" ")
pi_list = []
for i in range(len(clear_pi)):
    pi_list.append(len(clear_pi[i]))
print(pi_list)