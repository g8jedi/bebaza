from decimal import Decimal

# Employee Payroll Taxes
EMPLOYEE_TAX_SFS = Decimal(.0304)
EMPLOYEE_TAX_AFP = Decimal(.0287)
EMPLOYEE_TOTAL_TAXES = EMPLOYEE_TAX_SFS + EMPLOYEE_TAX_AFP

# Employer Liabilities
SFS_EMPLOYER_LIABILITY = Decimal(.0709)
AFP_EMPLOYER_LIABILITY = Decimal(.0710)
SRL_EMPLOYER_LIABILITY = Decimal(.0110)
INFOTEP_EMPLOYER_LIABILITY = Decimal(0.01)
TOTAL_EMPLOYER_LIABILITIES = SFS_EMPLOYER_LIABILITY + AFP_EMPLOYER_LIABILITY + SRL_EMPLOYER_LIABILITY + INFOTEP_EMPLOYER_LIABILITY

# RULES
HORAS_EXTRAS_RATE = Decimal(1.35)
HORAS_FERIADOS_RATE = Decimal(2.00)
SALARY_TO_DAILY_DIV = Decimal(23.83)