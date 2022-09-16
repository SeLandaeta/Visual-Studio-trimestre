deposit=float(input("Please write your total savings:"))
profit= deposit*0.04
year1= deposit+profit
year2=year1+profit
profit=year2*0.04
year3=year2+profit
print(f"in the first year you will earn {round (year1, 2)}")
print(f"in the second year you will earn {round (year2, 2)}")
print(f"in the third year you will earn {round (year3, 2)}")