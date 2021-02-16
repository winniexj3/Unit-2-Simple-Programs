b= balance = 3329
aR= annualInterestRate = 0.2
lowest=10
ba=b

while b>0:
    for m in range(12):
        mon_unpaid=b-lowest+(aR/12.0)*(b-lowest)
        b=mon_unpaid 
    if mon_unpaid>0:
        lowest+=10
        b=ba
    else:
        print("Lowest Payment:", lowest)
        

       


    

