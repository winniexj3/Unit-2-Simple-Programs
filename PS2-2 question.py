b= balance = 3329
aR= annualInterestRate = 0.2
lowest=10
m=0
ba=b

for m in range(12):
    mon_unpaid=b-lowest+(aR/12.0)*(b-lowest)
    b=mon_unpaid 
    if m==12 and mon_unpaid>0:
        lowest+=10
        b=ba
        m=1
    else:
        m+=1       
print("Lowest Payment:", lowest)

