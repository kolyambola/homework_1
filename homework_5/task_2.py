# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('task_2.txt') as my_file:
    my_file_lines = my_file.readlines()

str_count = 0

for ind, line in enumerate(my_file_lines, 1):
    str_count += 1
    words_count = len(line.split())
    print(f'{ind} строка - {words_count} слов(а)')
print(f'Всего {str_count} строк(и)')
