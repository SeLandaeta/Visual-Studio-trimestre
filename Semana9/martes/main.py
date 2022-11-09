def palabrainversa (palabra,indx):
    if palabra[indx] == 0 :
        return palabra [indx]

    return palabra[indx] + palabrainversa(palabra,indx - 1)

def main():

    word =input("Please enter a word:\n") 
    print(palabrainversa(word,len[word:-1]))
main()