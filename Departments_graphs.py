!pip install pyg-nightly
!pip install 'scipy>=1.8'

import json

import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt


# Открываем объединённый файл с данными
with open('merged_data.json', "r") as readFile:
    merge_data = json.load(readFile)

### Выделяем по ключам из .json отделы, задачи и ответственных сотрудников

departments = []
persons = []
tasks = []
for n in range(9999):
    try:
        for i in range (1,10):
            try:
              departments.append(merge_data[n]['Tasks']['Task{}'.format(i)]['task_responsibles_groups'])
              persons.append(merge_data[n]['Tasks']['Task{}'.format(i)]['task_responsibles_people'])
              tasks.append(merge_data[n]['Tasks']['Task{}'.format(i)]['task_text'])
            except KeyError:
                continue
            except IndexError:
                continue
    except IndexError:
        continue

### Находим уникальные значения департаментов,сотрудников и задач:

departments_set = set(departments)
departments_Unique_list = list(departments_set)
departments_Unique_list

persons_task_text_set = set(persons)
persons_Unique_list = list(persons_task_text_set)
len(persons_Unique_list)

tasks_set = set(tasks)
tasks_Unique_list = list(tasks_set)
len(tasks_Unique_list)

# Строим граф
DG = nx.DiGraph()

for g in range(int(len(departments_Unique_list))):
    try:
      DG.add_edge('ООО "Мегасофт"', departments_Unique_list[g]) 
      for i in range(int(len(persons_Unique_list))):
          DG.add_edge(departments_Unique_list[g], persons_Unique_list[i])  
          for t in range(425): #int(len(persons_Unique_list))):
                DG.add_edge(persons_Unique_list[g], tasks_Unique_list[t])
    except IndexError:
      continue

nx.draw(DG, with_labels=False, font_weight='bold')
