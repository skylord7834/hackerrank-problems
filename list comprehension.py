if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    final=[]
    for i in range(x+1):
        for j in range( y+1):
            for k in range(z+1):
                temp=[]
                if i+j+k != n:
                    temp.append(i)
                    temp.append (j)
                    temp.append(k)
                    final.append(temp)
    print(final)
