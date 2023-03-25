n=int(input('''\t\tpress 1 to convert currency
                press 2 to calculate BMI
                press 3 to convert temperature
                press 4 to calculate age
                press 5 to see calender
                press 6 to roll dice
                press 7 to use arithmetic calculator
                press 8 to generate random password
                press 9 to detect language
                press 10 to make QR code of link'''))
if n==1:
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()

    a= int(input("Enter the Amount:"))
    b=input("From Currency:").upper()
    x=input("To Currency: ").upper()


    ans=c.convert(b,x, a)

    print("Result=",ans)
elif n==2:
   
    height=float(input("Enter Your Height in cm:"))
    weight=float(input("Enter Your Weight in Kg:"))

    height=height/100

    BMI=weight/(height*height)

    print("Your Body Mass Index is:",BMI)
    if BMI>0:
       
        if BMI<=16:
       
            print("You are Severely Underweight")

        elif BMI<=18.5:
            print("You are underweight")

        elif BMI<=25:
            print("You are Healthy")

        elif BMI<=30:
            print("You are Overweight")

        else:
            print("very very high!")
elif n==3:
   
    n=int(input("for fehrenheight to celcius=1,celcius to ferhrenheight=2"))
    if n==1:
        Fehrenheight=int(input("Enter the Value of Fehrenheight:"))

        celsius=(Fehrenheight-32)*5/9

        print("celsius Value:",celsius)
       
    elif n==2:
        celsius=int(input("Enter the Value of celsius:"))

        Fehrenheight=(celsius*(9/5))+32

        print("Fehrenheight Value:",Fehrenheight)
    else:
        print("invalid operation")