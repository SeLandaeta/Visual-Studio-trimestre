#!!!!!!!!!!!!!!!!!! condicion de salida !!!!!!!!!!!!!!!!!
#no usar while o for dentro de mis funciones recursivas
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)