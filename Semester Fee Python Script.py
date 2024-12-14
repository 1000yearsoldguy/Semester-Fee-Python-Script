credit_value = 5000
trimester_registration_fee = 5000

print('\nIn UIU, each credit is BDT ' + str(credit_value) + ' and the trimester registration fee is BDT ' + str(trimester_registration_fee))
print("-----------------------------------------------------------------------------")

credits = int(input("How many credits have you taken in this trimester? : "))
installment_count = int(input("How many installments are there in this trimester? : "))

installments = input("Mention installment percentages (separated by spaces): ").split()
installments = [int(percentage) for percentage in installments]

if sum(installments) != 100:
    print("Error: Installment percentages must sum to 100.")
    exit()

preregistration_status = input("Is UIU taking the registration fee? (Yes/No): ").strip().lower()

total_fee = credit_value * credits
if preregistration_status in ['no', 'n']:
    print("-----------------------------------------------------------------------------")
    for i in range(len(installments)):
        if i == 0:
            installment_amount = (installments[i] / 100) * total_fee + trimester_registration_fee
            print(f"Installment Number {i + 1}: {installments[i]}% of total fee = {((installments[i] / 100) * total_fee):.2f} + {(trimester_registration_fee):.2f} = {(installment_amount):.2f}")
        else:
            installment_amount = (installments[i] / 100) * total_fee
            print(f"Installment Number {i + 1}: {installments[i]}% of total fee = {installment_amount:.2f}")

elif preregistration_status in ['yes', 'y']:
    registration_fee = int(input("How much is the registration fee this time? : "))
    remaining_fee = total_fee - registration_fee
    print("-----------------------------------------------------------------------------")
    print(f"Trimester Registration Fee: {registration_fee}")
    for i in range(len(installments)):
        installment_amount = (installments[i] / 100) * remaining_fee
        print(f"Installment Number {i + 1}: {installments[i]}% of remaining fee = {installment_amount:.2f}")
else:
    print("Error: Invalid input for preregistration status.")