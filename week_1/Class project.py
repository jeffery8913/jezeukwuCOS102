# PYTHON PROGRAM TO CALCULATE SIMPLE INTEREST, COMPOUND INTEREST, AND ANNUITY PLAN!

class FinancialCalculator:
    def simple_interest(self):
        r = float(input("What's your Rate (%)? "))
        t = float(input("What's the amount of time used (years)? "))
        p = float(input("What's the principal? "))
        
        a = p * (1 + (r / 100) * t)
        return a

    def compound_interest(self):
        r = float(input("What's your Rate (%)? "))
        t = float(input("What's the amount of time used (years)? "))
        p = float(input("What's the principal? "))
        n = float(input("How many times is interest compounded per year? "))

        a = p * (1 + r / (100 * n)) ** (t * n)
        return a

    def annuity_plan(self):
        pmt = float(input("What's the regular payment amount? "))
        r = float(input("What's your Rate (%)? ")) / 100  # Convert to decimal
        t = float(input("What's the amount of time (years)? "))
        n = float(input("How many times is interest compounded per year? "))

        d = (1 + r / n) ** (t * n)
        a = pmt * ((d - 1) / (r / n))
        return a


# Create an instance of the class
calculator = FinancialCalculator()

# Ask the user for the type of calculation
q = input("What do you want to Calculate? (si for Simple Interest, ci for Compound Interest, ap for Annuity Plan): ").strip().lower()

while q != 'exit':
    if q == 'si':
        result = calculator.simple_interest()
        print(f"Simple Interest: ${result:.2f}")

    elif q == 'ci':
        result = calculator.compound_interest()
        print(f"Compound Interest: ${result:.2f}")

    elif q == 'ap':
        result = calculator.annuity_plan()
        print(f"Annuity Plan: ${result:.2f}")

    else:
        print("INVALID KEYWORDS OR VALUES INPUTTED")

    q = input("What else do you want to do? (Type 'exit' to quit): ").strip().lower()