import random
from pprint import pprint
from types import new_class

from Tools.scripts.mailerdaemon import emparse_list_from

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученику по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести информацию по всем оценкам для определенного ученика
        5. Вывести средний балл по каждому предмету по определенному ученику
        6. Удалить оценку
        7. Добавить новый предмет
        8. Добавить ученика
        9. Редактирование ученика
       10. Изменение оценки
       11. Редактировать название предмета
       12. Удалить ученика
       13. Удалить предмет у ученика
       14. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам:')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Вывести информацию по всем оценкам для определенного ученикаgit init')
        student = input('Введите имя ученика:')
        print(student)
        for class_,marks in students_marks[student].items():
            if student in students_marks.keys():
                print(class_, marks)
            else:
                print('Ошибка: неверное имя ученика')


    elif command == 5:
            print('5. Вывести средний балл по каждому предмету по определенному ученику')
            name = input('Введите имя ученика:')
            if student in students_marks.keys():
                for classes,marks in students_marks[student].items():
                    marks_sum = sum(marks)
                    marks_count = len(marks)
                    print(f'{classes} - {marks_sum//marks_count}')

    elif command == 6:
        print('6. Удалить оценку:')
        name = input('Введите имя ученика у которго нужно удалить:')
        class_ = input('Введите предмет по которому нужно удалить оценку:')
        print(f'''{name}
            Оценки по: {class_} {students_marks[student][class_]}''')
        mark = int(input('Введите оценку которую нужно удалить: '))
        if name in students_marks.key() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student] [class_].remove(mark)
                print('Оценка удалена')
                print(f'''{name}
                {students_marks[student]}''')
            else:
                print('Оценки в списке нет')
    elif command == 7:
        print('7. Добавить новый предмет:')
        newclass = input('Введите название нового предмета: ')
        classes . append(newclass)
        for student_classes in students_marks.values():
            student_classes[newclass] = []
        print(f'Предмет {newclass} успешено добавлен.')

    elif command == 8:
        print('8. Добавить ученика:')
        student = input('Введите имя ученика:')
        if student in students:
                print('Данный студент уже присутсвует в списке')
        else:
            students.append(student)
            students.sort()
            print(f'Ученик {student} добавлен в список класса')
            print(F'Список класса: {students}')


    elif command == 9:
        print('9. Редактирование ученика:')
        student = input('Введите имя ученик:')
        newStudent = input('Введите новое имя:')
        if student in students_marks.keys():
            students_marks[newStudent] = students_marks[student]
            del students_marks[student]
            print(f'Имя {student} изменен на {newStudent}')
            print(f'''{newStudent}
                    {students_marks[newStudent]}''')
        else:
            print('Неправильное имя ученика:')


    elif command == 10:
        print('10. Изменение оценки:')
        student = input('Введите имя ученика для изменения оценки:')
        class_ = input('Введите нахвание предмета:')
        print(f'''{student}
             Оценки по : {class_} {students_marks[student][class_]}''')
        mark = int(input('Введите оценку которую нужно изменить:'))
        newMark = int(input('Введите новую оценку:'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                students_marks[student][class_].append(newMark)

                print(f'Оценка {student} по предмету {class_} изменена с {mark} на {newMark}' )
                print(f'''{student}
                     Оценка по: {class_} {students_marks[student][class_]}''')
            else:
                print('Такой оценки нет')

    elif command == 11:
        print('11. Редактировать название предмета:')
        class_ = input('Введите название предмета:')
        if class_ in classes:
            new_class_ = input('Введите новое название предмета: ')
            classes.append(new_class_)
            classes.remove(class_)
            for student in students:
                students_marks[student][new_class_] = students_marks[student][class_]
                del students_marks[student][class_]
                print(f'Предмет {class_} изменен на {new_class_}')
                print(f'Актуальный список предметов')
                print(classes)
                for student in students:
                    print(f'''{student}
                    {students_marks[student]}''')

    elif command == 12:
        print('12. Удалить ученика')
        student = input('Введите имя:')
        if student in students_marks.keys():
            del students_marks[student]
            print(student)
            print(students_marks)
        else:
            print('Данного ученика нет в списке')

    elif command == 13:
        print('13. Удалить предмет')
        student = input('Введите имя ученика для удаления предмета:')
        class_ = input('Введите предмет для удаления:')
        if class_ in (students_marks[student]).keys():
            students_marks[student][class_] = students_marks[student][class_]
            del students_marks[student][class_]
            print(f'Измененные предметы: {students_marks}')
        else:
            print('Предмет не найден')





    elif command == 14:
        print('14. Выход из программы')
        break




