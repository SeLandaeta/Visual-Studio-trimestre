#ejercicio cuenta
def dinero(account):
    for dinero in account:
        total = sum(dinero)
        print ("El cliente mas adinerado tine un total de:",total,"$")
    
def main():
    account=[(1,2,3),(3,2,1)]
    dinero(account)
main()