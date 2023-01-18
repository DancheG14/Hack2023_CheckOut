import json
import networkx as nx
import matplotlib.pyplot as plt

# Открываем объединённый файл с данными
with open('merged_data.json', "r") as readFile:
    merge_data = json.load(readFile)

# Определяем уникальные отделы
departments = []
for n in range(10000):
    departments.append(merge_data[n]['Tasks']['Task1']['task_responsibles_groups'])
    
# Определяем ФИО сотрудников
persons = []
for n in range(10000):
    departments.append(merge_data[n]['Tasks']['Task1']['task_responsibles_people'])




departments_set = set(departments)
departments_Unique_list = list(departments_set)

# Строим граф
DG = nx.DiGraph()

DG.add_edge('ООО "Мегасофт"', departments_Unique_list[0])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[1])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[2])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[3])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[4])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[5])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[6])
DG.add_edge('ООО "Мегасофт"', departments_Unique_list[7])

nx.draw(DG, with_labels=True, font_weight='bold')
