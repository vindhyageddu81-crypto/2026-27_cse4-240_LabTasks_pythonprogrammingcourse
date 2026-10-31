principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))

rate_of_interest_in_rupees = float(input("Enter rate of interest in percentage: "))

time_in_year = float(input("Enter time in years: "))

total_amount_in_rupees = principal_amount_in_rupees * (1 + rate_of_interest_in_rupees / 100) ** time_in_year

compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees

print(f"Compound interest is {compound_interest_in_rupees} rupees")