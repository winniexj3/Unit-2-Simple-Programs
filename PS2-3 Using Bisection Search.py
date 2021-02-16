b= balance 
aR= annualInterestRate 
Upper=(b*(1+aR/12.0)**12)/12.0
Lower=b/12.0
lowest=(Upper+Lower)/2.0
epsilon=0.01
balance_initial=b

while abs(b)>epsilon:
    lowest=(Upper+Lower)/2.0
    b=balance_initial        
    for month in range(12):
        b=b-lowest+((aR/12.0)*(b-lowest))
    if b>epsilon:
       Lower=lowest
    elif b<-epsilon:
        Upper=lowest
    else:
        break
print("Lowest Payment:",round(lowest,2))
    

       
        
    
    


