basic_pay = int(input("enter the basic salary of employee: ")) 
print("the basic salary of employee is: ",basic_pay) 
HRA=0.10*basic_pay
print("the HRA of Employee is:,HRA")
DA=1.2*basic_pay
print("the Dearness allowance of employee is:",DA)
TA=0.05*basic_pay
print("the Travelling allowance of employee is:",TA)
TS=basic_pay+HRA+DA+TA
print("the total salary of employee is:",TS)
PT=0.02*TS
print("the Professional tax of employee is:",PT)
NS=TS-PT
