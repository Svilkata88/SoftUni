companies_employee_data = {}
command = input().split(' -> ')

while command[0] != 'End':
    company, employee_id = command[0], command[1]
    if company not in companies_employee_data:
        companies_employee_data[company] = [employee_id]
    if employee_id not in companies_employee_data[company]:
        companies_employee_data[company].append(employee_id)
    command = input().split(' -> ')

for k, v in companies_employee_data.items():
    print(k)
    for index in range(len(v)):
        print(f'-- {v[index]}')
