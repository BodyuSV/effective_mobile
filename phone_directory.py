"""" Тестовое задание компании  effective mobile. Телефонный справочник"""
import math


class Abonent:
    def __init__(self, name, surname, patronymic, name_of_the_organization, work_phone, personal_telephone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.name_of_the_organization = name_of_the_organization
        self.work_phone = work_phone
        self.personal_telephone = personal_telephone

# ввод данных абонента
def input_info_abonent():
    new_abonent_name = input('Введите имя нового абонента')
    new_abonent_patronymic = input('введите отчество')
    new_abonent_surname = input('введите фамилию')
    new_abonent_name_of_the_organization = input('введите название организации')
    new_abonent_work_phone = input('введите рабочий телефон')
    new_abonent_personal_telephone = input('введите личный/мобильный телефон')
    new_abonent = Abonent(new_abonent_name, new_abonent_surname, new_abonent_patronymic,
                          new_abonent_name_of_the_organization, new_abonent_work_phone, new_abonent_personal_telephone)
    return new_abonent


# добавление абонента
def add_abonent():
    new_abonent = input_info_abonent()
    with open('db_telephone.txt', 'a', encoding='utf-8') as file_db:
        new_contact = (f'{new_abonent.name},{new_abonent.patronymic},{new_abonent.surname},'
                       f'{new_abonent.name_of_the_organization},'
                       f'{new_abonent.work_phone},{new_abonent.personal_telephone}\n')
    file_db.write(new_contact)

    return new_contact


# поиск абонента
def subscriber_search():
    search = input('ведите имя абонента. номер телефона или организацию')
    with open("db_telephone.txt", 'r', encoding='utf-8') as file:
        file_content = file.readlines()
    for line in file_content:
        if search.lower() in line.lower():
            print(line)


# редактирование записи
def edit_an_entry():
    search = input('введите номер абонента')
    with open("db_telephone.txt", 'r', encoding='utf-8') as file:
        file_content = file.readlines()
        for row in file_content:
            if search.lower() in row.lower():
                row = add_abonent()


# Вывод записей постранично
def show_page():
    with open("db_telephone.txt", 'r', encoding='utf-8') as file:
        data = file.readlines()
    contact_list = [contacts for contacts in data]
    max_page = math.ceil(len(contact_list) / 10)
    for page in range(0, max_page + 1):
        this_page = contact_list[page * 10 - 10: page * 10]
        for row in this_page:
            print(row)
        if input('ENTER: следующая страница / "x": Выход ').lower() == 'x':
            break

# главное меню
while True:
    print('1 - добавить абонента, 2 - поиск абонента, 3 - изменить запись в справочнике (для выбора записи используйте'
          ' номер телефона), 4 - просмот справочника постранично')
    select = input('выберите действие')
    if select == '1':
        add_abonent()
    if select == '2':
        subscriber_search()
    if select == '3':
        edit_an_entry()
    if select == '4':
        show_page()
    continue