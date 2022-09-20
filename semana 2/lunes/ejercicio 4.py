primer_numero=  (input ("por favor escriba un numero: "))
segundo_numero=  (input ("por favor escriba un segundo numero: "))
is_valid = True

if primer_numero.isnumeric:
    primer_numero=float(primer_numero)
else:
     is_valid=False

if segundo_numero.isnumeric:
    segundo_numero=float(segundo_numero)
else:
     is_valid=False


if is_valid: 
    if primer_numero/segundo_numero==0: 
        print ("error")

    else:
        print (primer_numero/segundo_numero)

else: print ("Error fatal")