def is_valid_passport(series, number):
    if len(series) != 4 or not series.isdigit():
        return False
    if len(number) != 6 or not number.isdigit():
        return False
    return True


def calc_pdn(income, monthly_payment):
    if income == 0:
        return None
    pdn = round((monthly_payment / income) * 100, 1)
    return pdn
    
def check_age(age):
    if age < 18 or age > 76:
        return 'reject'
    elif 18 <= age <= 22 or 61 <= age <= 76:
        return 'manual'
    else:
        return 'ok'


def check_overdue(has_overdue):
    if has_overdue == True:
        return 'reject'
    else:
        return 'ok'


def score_client(age, income, has_overdue, passport_series, passport_number, monthly_payment):
    if not is_valid_passport(passport_series, passport_number):
        return 'REJECT'


    age_status = check_age(age)
    overdue_status = check_overdue(has_overdue)


    if age_status == 'reject' or overdue_status == 'reject':
        return 'REJECT'
    elif age_status == 'manual' or overdue_status == 'manual':
        return 'MANUAL'
    else:
        return 'APPROVED'
series = input("Серия паспорта: ")
number = input("Номер паспорта: ")
age = int(input("Возраст: "))
income = int(input("Доход: "))
monthly_payment = int(input("Ежемесячный платёж: "))
has_overdue = input("Есть просрочка? (True/False): ").lower() == 'true'


decision = score_client(age, income, has_overdue, series, number, monthly_payment)
age_result = check_age(age)
overdue_result = check_overdue(has_overdue)
passport_result = is_valid_passport(series, number)
pdn_result = calc_pdn(income, monthly_payment)


print('=== ОТЧЁТ ПО КЛИЕНТУ ===')
print(f'Решение: {decision}')
print(f'Проверка возраста: {age_result}')
print(f'Проверка просрочки: {overdue_result}')
print(f'Проверка паспорта: {passport_result}')
print(f'ПДН: {pdn_result}%')
