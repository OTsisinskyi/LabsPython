import re


def main():
    open_file = open(".\\apache_logs.txt", "r")
    read_file = open_file.read()

    search_pattern = r"\[[1][789]\/May\/2015:" \
                     r"(?:10|11|12|13|14|15|16|17|18|19|20|21|22|23):05:(?:(?!02)[0-9][0-9]).+\"GET.+" \
                     r"(?:png|jpeg|jpg|gif)\sHTTP/1.1\"\s200\s(\d+)"
    my_file = re.findall(search_pattern, read_file)
    my_file_int = [int(x) for x in my_file]
    summa = sum(my_file_int) / (1024 * 1024)
    return print(f"Загальний розмір файлів: {summa} мегабайт")


if __name__ == '__main__':
    main()
