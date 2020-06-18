def abcSalarySystem(salesExecutiveName,executiveCategory,employeeNumber,basicSalary,weekOneAmount,weekTwoAmount,weekThreeAmount,weekFourAmount):
    TotalSalesOfTheMonth = (weekOneAmount + weekTwoAmount + weekThreeAmount + weekFourAmount)

    # CATEGORY A
    
    if (executiveCategory == "A") or (executiveCategory == "a"):
        if (TotalSalesOfTheMonth < 100000):
            incentiveAmount = 2500
            commissionAmount = (TotalSalesOfTheMonth / 100) * 2
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth < 250000) and (TotalSalesOfTheMonth > 100000):
            incentiveAmount = 4000
            commissionAmount = (TotalSalesOfTheMonth / 100) * 2.5
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth > 250000):
            incentiveAmount = 5000
            commissionAmount = (TotalSalesOfTheMonth / 100) * 3
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))

    # CATEGORY B

    elif (executiveCategory == "B") or (executiveCategory == "b"):
        if (TotalSalesOfTheMonth < 75000):
            incentiveAmount = 1000
            commissionAmount = (TotalSalesOfTheMonth / 100) * 1.5
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth < 150000) and (TotalSalesOfTheMonth > 75000):
            incentiveAmount = 2000
            commissionAmount = (TotalSalesOfTheMonth / 100) * 2
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth > 150000):
            incentiveAmount = 2500
            commissionAmount = (TotalSalesOfTheMonth / 100) * 2.5
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))



    # CATEGORY C

    elif (executiveCategory == "C") or (executiveCategory == "c"):
        if (TotalSalesOfTheMonth < 25000):
            incentiveAmount = 500
            commissionAmount = (TotalSalesOfTheMonth / 100) * 0
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth < 50000) and (TotalSalesOfTheMonth > 25000):
            incentiveAmount = 1000
            commissionAmount = (TotalSalesOfTheMonth / 100) * 1
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))


        elif (TotalSalesOfTheMonth > 50000):
            incentiveAmount = 1500
            commissionAmount = (TotalSalesOfTheMonth / 100) * 1.5
            TotalSalary = (basicSalary + incentiveAmount + commissionAmount)

            print("____________________________________________________________________")
            print("               ABC Company (PVT) Ltd – SALARY SLIP                  ")
            print("====================================================================")
            print("[!] Employee Name                        : " + salesExecutiveName)
            print("[!] Employee Number                      : " + str(employeeNumber))
            print("[!] Basic salary                         : " + str(basicSalary))
            print("[!] Monthly Sales Amount                 : " + str(TotalSalesOfTheMonth))
            print("[!] Incentive                            : " + str(incentiveAmount))
            print("[!] Commission                           : " + str(commissionAmount))
            print("[!] Total Salary                         : " + str(TotalSalary))

    else:
        print("____________________________________________________________________")
        print("[ERROR] : Invalid Category Type! Enter (A, B, C)")

# USER INPUTS

x=0
while(x < 1):
    print("____________________________________________________________________")
    print("                      $ ABC SALARY SYSTEM $                         ")
    print("--------------------------------------------------------------------")

    SEN=input("[!] > Enter Sales Executive Name         : ")
    CTGY=input("[!] > Executive Category Type (A, B, C)  : ")
    ENUM=input("[!] > Employee Number                    : ")
    BSLRY=int(input("[!] > Basic Salary                       : "))
    W1=int(input("[!] > Week One Sale Amount               : "))
    W2=int(input("[!] > Week Two Sale Amount               : "))
    W3=int(input("[!] > Week Three Sale Amount             : "))
    W4=int(input("[!] > Week Four Sale Amount              : "))        

    abcSalarySystem(SEN,CTGY,ENUM,BSLRY,W1,W2,W3,W4)
    print("====================================================================")
    print("|||||||||||||||||||||||||| NEXT EMPLOYEE |||||||||||||||||||||||||||")




