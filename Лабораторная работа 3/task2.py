# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator = ','):
    first_list = first_group.split(separator)
    second_list = second_group.split(separator)
    first_set = set(first_list)
    our_intersection = first_set.intersection(set(second_list))
    our_list = list(our_intersection)
    our_list.sort()
    return our_list



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"Общие участники:{find_common_participants(participants_first_group, participants_second_group, '|')}")
