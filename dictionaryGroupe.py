users = ['zaxar', 'vadim']
books = ['python', 'gamer']
dictionary = [['zaxar', 'python'], ['vadim', 'gamer']]


def readers_search():
    user_name = input('Введите имя читателя: ')

    for i in users:
        if i == user_name:
            return f'Читатель {user_name} найден'
    return f'Читатель {user_name} не найден'


def book_search():
    book_name = input('Введите название книги: ')
    for i in books:
        if i == book_name:
            return f'Книга {book_name} найдена'
    return f'Книга {book_name} не найдена'


def new_reader():
    user_name = input('Введите имя нового читателя: ')
    users.append(user_name)
    user_number = input('Введите номер телефона:')
    users.append (user_number)
    user_street = input ('Адрес:')
    users.append (user_street)

    return f'Читатель {user_name} успешно зарегистрирован'


def new_book():
    book_name = input('Введите название новой книги: ')
    books.append(book_name)
    return f'Книга {book_name} успешно добавлена'


def get_book():
    user_name = input('Введите имя читателя: ')
    if user_name in users:
        book_name = input('Введите название книги: ')
        if book_name in books:
            dictionary.append([user_name, book_name])
            books.remove(book_name)
            return f'Читатель {user_name} взял книгу {book_name}'
        else:
            return 'Такой книги нет в базе'
    else:
        return 'Такого читателя нет в базе'


def return_book():
    user_name = input('Введите имя читателя: ')
    book_name = input('Введите название книги: ')
    counter = 0
    for i in dictionary:
        if i[0] == user_name and i[1] == book_name:
            del dictionary[counter]
            books.append(book_name)
            return f'Читатель {user_name} отдал книгу {book_name}'
        counter += 1
    return 'Неверно указан имя читателя или название книги'


def output_readers():
    users_output = []
    for i in dictionary:
        users_output.append(i[0])
    users_output = list(set(users_output))
    return users_output


while True:
    print(' ')
    print('1. Создание читателя')
    print('2. Создание новой книги книги')
    print('3. Поиск читателя')
    print('4. Поиск книги')
    print('5. Выдача книги')
    print('6. Прием книги обратно')
    print('7. Вывод должников')
    print('8. Выход\n')
    try:
        user_choice = int(input('Введите команду: '))

        if user_choice == 3:
            print(readers_search())
        elif user_choice == 4:
            print(book_search())
        elif user_choice == 1:
            print(new_reader())
        elif user_choice == 2:
            print(new_book())
        elif user_choice == 5:
            print(get_book())
        elif user_choice == 6:
            print(return_book())
        elif user_choice == 7:
            print(output_readers())
        elif user_choice == 8:
            break
    except ValueError:
        print('Мне нужен выбор (цифрой)')
