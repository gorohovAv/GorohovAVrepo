# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r',) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        json_string = json.dumps(list(reader), indent=4)
        #print(json_string, end='')
        with open(OUTPUT_FILENAME, 'w') as json_file:
            json_file.write(json_string)






if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
