import os

# Получаю абсолютный путь к папке sorted
folder = os.path.join(os.getcwd(), 'sorted')

# Получаю список файлов в директории folder с абсолютными путями
files_list = []
for root, dirs, files in os.walk(os.path.abspath(folder)):
    for file in files:
        files_list.append(os.path.join(root, file))

# Открываю файлы по очереди. Использую enumerate для получения индекса файла в списке files_list
for i, file in enumerate(files_list):
    with open(file, 'r', encoding='utf-8') as input_file:
        # Считаю количество строк в файле при помощи enumerate
        for count, _ in enumerate(input_file, 1):
            pass
        # Изменяю элемент списка files_list по индексу i
        # По сути добавляю к имени файла количество строк в файле
        # Использую кортеж
        files_list[i] = (file, count)

# Можно было использовать len(input_file.readlines()) и сохранять сразу текст файла в переменную
# но если файлы будут слишком большими, то, вероятно, это будет занимать много памяти.

# for i, file in enumerate(files_list):
#     with open(file, 'r', encoding='utf-8') as input_file:
#         text = input_file.readlines()
#         files_list[i] = (file, len(text), text)


# В моей реализации, вероятно, памяти занимать будет меньше, но придется повторно открывать файлы.
# Какую реализацию лучше использовать на практике???

#  Сортирую по количеству строк в файле(по второму элементу кортежа),
#  а при совпадении элементов по пути файла (по первому элементу)
files_list.sort(key=lambda x: (x[1], x[0]))
# print(*files_list, sep='\n')


with open(os.path.join(os.getcwd(), 'result.txt'), 'a', encoding='utf-8') as out_file:
    for file, count in files_list:
        with open(file, 'r', encoding='utf-8') as input_file:
            out_file.write(file + '\n')
            out_file.write(str(count) + '\n')
            for line in input_file:
                if not line.endswith('\n'):
                    line += '\n'
                out_file.write(line)
