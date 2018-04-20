col1 = open('col1.txt')
col2 = open('col2.txt')
col3 = open('col3.txt','w')
with col1 as left , col2 as right:
    for line_left,line_right in zip(left,right):
        string = "%s\t%s" % (line_left,line_right)
        string = string.replace('\n','')
        col3.write(string + "\n")
col3.close()