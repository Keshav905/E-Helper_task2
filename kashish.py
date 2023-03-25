elif n==4:
    def ageCalculator(y,m,d):
        import datetime
        today = datetime.datetime.now().date()
        dob = datetime.date(y,m,d)
        age = int((today-dob).days / 365.25)
        print(age)
    y=int(input("Enter year of birth:"))
    m=int(input("Enter month of birth:"))
    d=int(input("Enter date of birth:"))
    ageCalculator(y,m,d)
elif n==5:
    import calendar
    year=int(input("Enter the year:"))
    cal=calendar.calendar(year)
    print(cal)
elif n==6:
    import random
    x="y"

    while x=="y":
        random_number=random.randint(1,6)
   
        if random_number==1:
            print("[---------]")
            print("[         ]")
            print("[    *    ]")
            print("[         ]")
            print("[---------]")

        elif random_number==2:
            print("[---------]")
            print("[  *      ]")
            print("[         ]")
            print("[      *  ]")
            print("[---------]")

        elif random_number==3:
            print("[---------]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[---------]")

        elif random_number==4:
            print("[---------]")
            print("[ *     * ]")
            print("[         ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number==5:
            print("[---------]")
            print("[ *     * ]")
            print("[    *    ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number==6:
            print("[---------]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[---------]")

        x=input("Press y to Roll Again and Press Any Other Key for Exit:")
elif n==7:
    num1=int(input("Enter the First Number:"))
    oper=input("Enter the Operation:")
    num2=int(input("Enter the Second Number:"))

    if oper=="+":
        sum=num1+num2
        print("The Answer is:",sum)

    elif oper=="-":
        subs=num1-num2
        print("The Answer is:",subs)

    elif oper=="*":
        mul=num1*num2
        print("The Answer is:",mul)

    elif oper=="/":
        div=num1/num2
        print("The Answer is:",div)

    else:
        print("Wrong Operation Input!")

    print("=========================\n")