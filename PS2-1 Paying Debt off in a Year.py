b= balance = 484
aR= annualInterestRate = 0.2
mR= monthlyPaymentRate = 0.04
i=1
nb=b-b*mR
for i in range(13):
    if i==1:
        b==nb
        i+=1
    else:
        b=nb+(aR/12.0)*nb
        nb=b-b*mR
        i+=1
print("Remaining balance:",round(b,2))
        
    

