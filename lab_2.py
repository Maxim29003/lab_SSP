import random

def gener_file(num_values, sort):
    filename = "Lab_2.txt"

    with open(filename, "w") as file:
        file.write(sort + "\n") 
        file.write(str(num_values) + "\n") 
        for _ in range(num_values):
            random_number = random.randint(1, 1000)
            file.write(str(random_number) + "\n")

    print(f"Сгенерирован файл '{filename}' с {num_values} случайными числами.")



def read_file(filename):
     with open(filename, "r") as file:
         numbers = file.readlines()
     return (list(map(lambda number: eval(number), numbers[2:])), numbers[0][:-1])


def write_file(data, filename):
      sort = data[1]
      mas = data[0]
      if sort == 'по возрастанию':
          mas.sort()
      elif sort == 'по убыванию':
          mas.sort(reverse=True)
      with open(filename, "w") as file:
        for elment in mas:
            file.write(str(elment) + "\n")


def main(n, sort):
    gener_file(n,sort)
    data = read_file("Lab_2.txt")
    write_file(data, "Lab_2_out.txt")

#main(20, 'по возрастанию')
main(20, 'по убыванию')


