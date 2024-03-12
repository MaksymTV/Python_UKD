def century(year):

  if year <= 0:
    raise ValueError("Рік не може бути від'ємним")
  return (year // 100) + (1 if year % 100 > 0 else 0)

year = 1900
century_number = century(year)
print(f"Рік {year} належить до {century_number} століття")

year = 2023
century_number = century(year)
print(f"Рік {year} належить до {century_number} століття")
