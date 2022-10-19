#imports math operator
import math 

#displays menu options for the user
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n\ninvestment - to calculate the amount of interest you'll earn on your investment \n"
      "bond       - to calculate the amount you'll have to pay on a home loan \n")


#prompts user to select a finance option
finance_option = (str(input("Please choose your option (investment / bond)?")))

#sets total amount to 0
Total_amount = 0

#Executes when user selects "investment"
if finance_option == "investment":

    #requests user for further details on the option selected
    deposit = (float(input("Please enter the amount you wish to deposit? R")))
    interest_rate = (int(input("Please enter the interest rate? ")))
    investment_term = (int(input("Please enter the amount of years you wish to invest? ")))
    interest = (str(input("Please choose your interest option (simple / compound)?")))

    #checks which interest option user selected
    if interest.strip().lower() == "simple":

        rate =  interest_rate / 100

        Total_amount = deposit *(1 + rate * investment_term)

        print ("Your investment of R",deposit,"over",investment_term,"years at",interest,"% annually choosing",interest,"will be R",round(Total_amount,2))

    else:

    
            rate =  interest_rate / 100
            
            Total_amount = deposit * pow((1 + rate),investment_term)
            
            #prints the total investment based on the users selecton
            print ("Your investment of R",deposit,"over",investment_term,"years at",interest,"choosing",interest,"will be R",round(Total_amount,2))
            
#executes if user selects bond and calculates monthly bond repayments
elif finance_option == "bond":

    Monthly_Repayment = 0
    
    property_value = (float(input("Please enter the value of the house? R")))
    annual_interest_rate = (float(input("Please enter the interest rate? ")))
    investment_term = (int(input("Please enter the number of months you wish to repay? ")))

    rate = annual_interest_rate / 100

    Monthly_Repayment = (rate/12 * property_value)/(1 - math.pow((1 + rate/12), -investment_term))
    
    #prints monthly bond repayments based on the users terms inserted
    print("Your monthly bond repayments for a house valued at R",property_value,"at",annual_interest_rate,"% annualy over",investment_term,"months will be R",round(Monthly_Repayment,2),"PM")
    

    
