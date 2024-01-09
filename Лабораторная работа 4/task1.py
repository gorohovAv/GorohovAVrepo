import json

# TODO решите задачу
def task() -> float:
    final_sum = 0
    with open('input.json', 'r') as file:
        input_data = json.load(file)
    for i in input_data:
        final_sum += i.get("score")*i.get("weight")
    return round(final_sum, 3)


print(task())
