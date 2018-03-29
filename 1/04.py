# 04. 元素記号
element = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans = {}
clear_element = element.replace(",", "").replace(".", "").split(" ")
branch = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i in range(len(clear_element)):
    if i in branch:
        ans[i] = clear_element[i][0:1:1]
    else:
        ans[i] = clear_element[i][0:2:1]
print(ans)