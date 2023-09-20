
"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# task 1
print('Названия отделов:')
for department in departments:
    print(department['title'])

print()
# task 2
employers = []
for department in departments:
    for employer in department['employers']:
        employers.append(employer['first_name'])
print('Имена сотрудников: ', ', '.join(employers))

print()
# task 3
employers = []
for department in departments:
    for employer in department['employers']:print()

print()
# task 4
employers_with_100k = []
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 100000:
            employers_with_100k.append(employer['first_name'])
print('Имена сотрудников, которые получают больше 100к: ', ', '.join(employers_with_100k))

print()
# task 5
position = []
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] < 80000:
            position.append(employer['position'])
print('Позиции с ЗП менее 80к: ', ', '.join(position))

print()
# task 6
expenses = 0
for department in departments:
    for employer in department['employers']:
        expenses += employer['salary_rub']
    print(f'Затраты на отдел {department["title"]} составляют {expenses} в месяц')
    expenses = 0

print()
# task 7
min_salary = []
for department in departments:
    for employer in department['employers']:
        min_salary.append(employer['salary_rub'])
    print(f'Минимальная зарплата в {department["title"]} составляет {min(min_salary)}')
    min_salary = []

print()
# task 8
salary = []
for department in departments:
    for employer in department['employers']:
        salary.append(employer['salary_rub'])
    print(f'Минимальная зарплата в {department["title"]} составляет {min(salary)}')
    print(f'Средняя зарплата в {department["title"]} составляет {sum(salary) / len(salary)}')
    print(f'Максимальная зарплата в {department["title"]} составляет {max(salary)}')
    print()
    salary = []

print()
# task 9
salary = []
for department in departments:
    for employer in department['employers']:
        salary.append(employer['salary_rub'])
print(f'Средняя зарплата в компании составляет {sum(salary) / len(salary)}')

print()
# task 10
position = []
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 90000:
            position.append(employer['position'])
position = set(position)
print('Позиции с ЗП более 90к: ', ', '.join(position))

print()
# task 11
salary_girls = []
for department in departments:
    for employer in department['employers']:
        if employer['first_name'] == 'Michelle' or employer['first_name'] == 'Nicole' or employer['first_name'] == 'Christina' or employer['first_name'] == 'Caitlin':
            salary_girls.append(employer['salary_rub'])
    print(f'В отделе {department["title"]} средняя зарплата девушек составляет: {round((sum(salary_girls) / len(salary_girls)), 2)}')
    salary_girls = []

print()
# task 12
names = []
for department in departments:
    for employer in department['employers']:
        name = employer['first_name']
        if name[-1] in 'aeiouy':
             names.append(name)
names = set(names)
print('Имена сотрудников, заканчивающиеся на гласную букву: ', ', '.join(names))

print()
# task 13
taxes = {'taxes': taxes}
departments_and_taxes = departments.copy()
for i in departments_and_taxes:
    i['taxes'] = taxes['taxes']

all_taxes = []

for department in departments_and_taxes:
    for employer in department['employers']:
        for tax in department['taxes']:
            all_taxes.append(employer['salary_rub'] * tax['value_percents'] / 100)
    print(f'Средний налог отдела {department["title"]} составляет {sum(all_taxes) / len(all_taxes)}')


print()
# task 14
employer_with_salary = []
for department in departments_and_taxes:
    for employer in department['employers']:
            if department['title'] == 'HR department':   
                print(f'Отдел {department["title"]}. ' 
                      f'Зарплата {employer["first_name"]} составляет: с учетом налогов {employer["salary_rub"]},'
                      'без учета налогов' 
                      f'{employer["salary_rub"] + (employer["salary_rub"] * 0.13 + employer["salary_rub"])}')
            elif department['title'] == 'IT department': 
                print(f'Отдел {department["title"]}. ' 
                      f'Зарплата {employer["first_name"]} составляет: с учетом налогов {employer["salary_rub"]},'
                      'без учета налогов ' 
                      f'{employer["salary_rub"] + (employer["salary_rub"] * 0.13 + employer["salary_rub"] * 0.06)}')     

print()
# task 15
monthly_tax_burden_HR = []
monthly_tax_burden_IT = []
for department in departments_and_taxes:
    for employer in department['employers']:
        if department['title'] == 'HR department':
            monthly_tax_burden_HR.append(employer['salary_rub'] * 13 / 100)
        elif department['title'] == 'IT department':
            monthly_tax_burden_IT.append(employer['salary_rub'] * (13 / 100 + 6 / 100))
HR_burden = sum(monthly_tax_burden_HR)
IT_burden = sum(monthly_tax_burden_IT)
if IT_burden > HR_burden:
    print(f'Налоговая нагрузка в HR department составляет {HR_burden} рублей'
          f'в IT department составляет {IT_burden} рублей')
else:
    print(f'Налоговая нагрузка в IT department составляет {IT_burden} рублей'
          f'в HR department составляет {HR_burden} рублей')
    
print()
# task 16
tax_more_100k = []
for department in departments_and_taxes:
    for employer in department['employers']:
            if department['title'] == 'HR department':
                if (employer['salary_rub'] * 13 / 100 * 12) > 100000:
                    tax_more_100k.append(employer['first_name'])
            elif department['title'] == 'IT department': 
                if (employer['salary_rub'] * (13 / 100 + 6 / 100) * 12) > 100000:
                    tax_more_100k.append(employer['first_name'])
print('Список сотрудников, за которых компания платит более 100к налогов в год: ', ', '.join(tax_more_100k))

print()
# task 17
min_tax = [10000000000]
min_taxes_emp = []
for department in departments_and_taxes:
    for employer in department['employers']:
        if department['title'] == 'HR department':
            tax_emp = employer['salary_rub'] * (13 / 100)
            if tax_emp < min_tax[0]:
                min_tax.clear()
                min_tax.append(tax_emp)
                min_taxes_emp.clear()
                min_taxes_emp.append(employer['first_name'])
                min_taxes_emp.append(employer['last_name'])
        elif department['title'] == 'IT department':
            tax_emp = employer['salary_rub'] * (13 / 100 + 6 / 100)
            if tax_emp < min_tax[0]:
                min_tax.clear()
                min_tax.append(tax_emp)
                min_taxes_emp.clear()
                min_taxes_emp.append(employer['first_name'])
                min_taxes_emp.append(employer['last_name'])
print('Минимальные налоги компания платит за ', ' '.join(min_taxes_emp))