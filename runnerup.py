# The first line contains n . The second line contains an array   of  integers each separated by a space
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    new=sorted(arr)
    remDupl=[]
    for i in range(n):
        if new[i] not in remDupl:
            remDupl.append(new[i])
    print(remDupl[-2])
