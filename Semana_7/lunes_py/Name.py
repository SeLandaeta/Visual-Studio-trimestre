
class vehicle:
    seller = 1
    def __init__ (self,brand,model,color,year):
        self.__brand = brand 
        self.model = model
        self.color = color
        self.year = year

    def get_color(self):
        return self.__brand 
        
    def get_color(self,brand):
        self.__brand = brand 
        
    def get_color(self):
        return self.color
        
    def print_color (self):
        print("El color es: ",self.color)
