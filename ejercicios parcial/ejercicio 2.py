#ejercicio replace

def remplazo():
    word = input("Please enter the replacing word")
    word2=word.replace("()","o")
    word3=word2.replace("(al)","al")
    print (word3)

def main():
    remplazo()
main()