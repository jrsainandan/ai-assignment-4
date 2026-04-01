import itertools

def solve(word1,word2,result):
    letters=set(word1+word2+result)
    letters=list(letters)
    digits=range(10)

    if len(letters)>10:
        return None

    for perm in itertools.permutations(digits,len(letters)):
        d=dict(zip(letters,perm))

        if d[word1[0]]==0 or d[word2[0]]==0 or d[result[0]]==0:
            continue

        n1=0
        for ch in word1:
            n1=n1*10+d[ch]

        n2=0
        for ch in word2:
            n2=n2*10+d[ch]

        n3=0
        for ch in result:
            n3=n3*10+d[ch]

        if n1+n2==n3:
            return d

    return None

def main():
    word1=input("Enter first word: ")
    word2=input("Enter second word: ")
    result=input("Enter result word: ")

    solution=solve(word1,word2,result)

    if solution:
        for k in solution:
            print(k,":",solution[k])
    else:
        print("No solution")

if __name__=="__main__":
    main()
