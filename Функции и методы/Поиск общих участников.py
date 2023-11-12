# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    participants_first_group = set(group1.split(separator))
    participants_second_group = set(group2.split(separator))
    common_participants = participants_first_group.intersection(participants_second_group)
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
