documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "2207 876237"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

command = input('Команды:\n p - определить владельца документа\n s - найти документ на полке\n l - '
                'получить список всех документов\n a - добавить новый документ\n '
                'o - вывести имена всех владельцев документов\n Введите команду:')


def document_owner():
    document_number = input("Введите номер документа:")
    for elements in documents:
        if elements['number'] == document_number:
            return f'Владелец документа - {elements["name"]}.'


def shelf_number():
    document_number = input("Введите номер документа:")
    for shelves, numbers in directories.items():
        if document_number in numbers:
            return f'Документ находится на полке {shelves}.'
    return 'Такого документа нет на полке. Проверьте введенный номер еще раз.'


def order():
    for elements in documents:
        print(f"{elements['type']} {elements['name']} {elements['number']} ")


def add_document():
    document_number = input('Номер документа:')
    document_owners = input('Владелец документа:')
    document_type = input('Тип документа:')
    document_shelf = input('На какую полку поместить документ?')
    if document_shelf not in directories.keys():
        return 'Такой полки не существует.'
    else:
        for keys, values in directories.items():
            if keys == document_shelf:
                values.append(document_number)
                # print(directories)
        new = dict()
        documents.append(new)
        new["type"] = document_type
        new["number"] = document_number
        new["name"] = document_owners
        # print(documents)
        return 'Документ добавлен'


def our_input(command):
    if command == "p":
        print(document_owner())
    elif command == "s":
        print(shelf_number())
    elif command == "l":
        order()
    elif command == "a":
        print(add_document())
    elif command == 'o':
        all_owners()


def all_owners():
    owners = []
    for elements in documents:
        try:
            owners.append(elements["name"])
        except KeyError:
            print(f'У документа {elements["number"]} отсутствует владелец.')
    print(owners)


our_input(command)
