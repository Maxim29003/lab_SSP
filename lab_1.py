import random

def task_1():
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    random_values = [random.uniform(0.0, 100.0) for _ in range(12)]

    for i in range(12):
        print(f"{months[i]}: {random_values[i]}")

   
    average = sum(random_values) / len(random_values)
    print(f"Среднее значение: {average}")

def task_2():
    # Создаем массив с датами в формате "месяц/день/год"
    dates = ["01/01/2022", "02/15/2022", "03/25/2022", "04/10/2022", "05/20/2022", "06/05/2022", "07/30/2022", "08/12/2022", "09/03/2022", "10/18/2022"]

    # Создаем словарь для преобразования числовых месяцев в текстовые
    month_names = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }

    # Проходим по каждой дате в массиве и выводим ее в новом формате
    for date in dates:
        parts = date.split("/")  # Разбиваем строку на части
        day = parts[1]
        month = month_names.get(parts[0], "неверный месяц")  # Преобразуем числовой месяц в текстовый
        year = parts[2]
        formatted_date = f"{day} {month} {year}"
        print(formatted_date)

def task_3(n):
    def generate_consonant():
        consonants = "БВГДЖЗКЛМНПРСТФХЦЧШЩ"
        return random.choice(consonants)
    
    str = ''
    for _ in range(0, n):
        str += generate_consonant()

    print(str)

def task_4(str):
    vowel_letters = "аеёиоуыэюя"
    print('Len = ', len(str))

    count_vowel = 0 

    for letter in vowel_letters: 
        count_vowel += str.count(letter)

    count_space = str.count(' ')

    print('Count_vowel = ', count_vowel)
    print('Count_space = ', count_space if count_space else 0)


def task_5(delimiter):
   string_array = ["Привет", "Мир", "Это", "Массив", "Строк"]
   str = ''

   for element in string_array:
       str += element
    
   if delimiter == '' : 
       print('Error delimiter = "" ') 
   else:
       print(str.split(delimiter))


   

    








