data = {}
while (True):
    data_key= input ("Please enter what data you want to safe: ")
    data_value = input ("Please enter the value you want to save: ")
    data[data_key] = data_value

    for datos , valor in data.items():
        print (f'Yur {datos} is {valor}')
    
    if input ("Do you want to exit? : \n Y-yes \n N-no") == "Y": 
        break
