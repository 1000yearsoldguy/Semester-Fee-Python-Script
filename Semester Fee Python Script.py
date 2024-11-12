credit_value = trimester_registration_fee = 5000

print('\nIn UIU each credit is BDT ' + str(credit_value) + ' and '+ 'per trimester registration fee is BDT '+ str(trimester_registration_fee))
print("-----------------------------------------------------------------------------")

credits = int(input("How many credits have you taken in this trimester? : "))
installment_count = int(input("How many installments are there in this trimester? : "))

installments = str(input("Mention installments (Separated by spaces) : ")).split()
    
preregistration_status = input("Is UIU taking Registration of fee? : ")

sum = ((credit_value*credits)+trimester_registration_fee)

if (preregistration_status == 'No' or 'no'or 'n' or 'N'):
    for i in range (len(installments)):
        print("Installment Number " + str(i+1) +" : "+ str((int(installments[i])/100)*sum))

elif (preregistration_status == 'yes' or 'Yes'or 'y' or 'Y'):
    registration_fee = int(input("How much is Registration Fee this time? : "))
    sum = sum - registration_fee
    for i in range (len(installments)):
        if i == 0 : print("Trimester Registration Fee : " + str(registration_fee))
        print("Installment Number " + str(i+1) +" : "+ str((int(installments[i])/100)*sum))