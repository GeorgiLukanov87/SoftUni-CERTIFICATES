n = int(input())

dashes = 2*n-4-(n//2)*2

print('/'+'^'*(n//2)+'\\'+'_'*dashes+'/'+'^'*(n//2)+'\\')

space = 2*n-2

for row in range(0, n-2):
    if row == n-3:
        print('|'+' '*(n//2)+' '+'_'*dashes+' '+' '*(n//2)+'|')
    else:
        print('|'+' '*space + '|')

print('\\'+'_'*(n//2)+'/'+' '*dashes+'\\'+'_'*(n//2)+'/')
