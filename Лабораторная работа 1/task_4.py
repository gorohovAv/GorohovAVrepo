users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = set(users)
vizits = {"Общее количество": 0, "Уникальные посещения": 0}
vizits["Общее количество"] = len(users)
vizits["Уникальные посещения"] = len(unique_users)
print(vizits)
