import re

START = r"17/May/2015:10:05:03"
END = r"19/MAY/2015:21:05:23"

input_filename = ".\\apache_logs.txt"
result_filename = "required period.txt"


def search_for_desired_period():
    input_file = open(input_filename, "r")
    result_file = open(result_filename, mode="w")
    my_text = input_file.readlines()

    for line in my_text:
        if re.findall(START, line) != None:
            result_file.write(line + '\n')

        if re.search(r"19/May/2015:21:05:23", line) != None:
            break
    input_file.close()
    result_file.close()


def main():
    count = 0
    required_period = open("required period.txt", "r")
    file = required_period.read()

    pattern = r"\"GET.+(?:png|jpeg|jpg|gif)\sHTTP/1.1\"\s200\s(\d+)"

    list_of_file_size = re.findall(pattern, file)
    for _ in list_of_file_size:
        count += 1

    my_file_int = [int(x) for x in list_of_file_size]
    summa = sum(my_file_int) / (1024 * 1024)
    required_period.close()
    return print(f"Загальний розмір файлів: {summa} Mб\nКількість: {count}")


if __name__ == '__main__':
    search_for_desired_period()
    main()
