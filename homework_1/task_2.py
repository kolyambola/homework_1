# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк

seconds = int(input('Введите время в секундах '))

seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f'Time: {hours:02}:{minutes:02}:{seconds:02}')
