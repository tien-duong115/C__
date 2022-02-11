def mcd(m, n):
    if m == n:
        return m
    if m > n:
        return mcd(m-n, n)
    else:
        return mcd(m, n-m)







if __name__ =="__main__":
    
    print(mcd(100,34))