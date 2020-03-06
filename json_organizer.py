import json

with open('source_file_2.json') as f:
    data = json.load(f)

managers_list = []
watchers_list = []
all_projects_managers_list = []
all_projects_watchers_list = []

for project in data:
    for manager in project['managers']:
        if manager not in managers_list:
            managers_list.append(manager)
    
    for watcher in project['watchers']:
        if watcher not in watchers_list:
            watchers_list.append(watcher)

for manager in managers_list:
    individual_projects_managers_list = []
    for project in data:
        if manager in project['managers']:
            project_dict = {'project': {'name': project['name'], 'priority': project['priority']}}
            individual_projects_managers_list.append(project_dict)
    individual_projects_managers_list = sorted(individual_projects_managers_list, key=lambda k: k['project']['priority'])
    all_projects_managers_list.append(individual_projects_managers_list)

for watcher in watchers_list:
    individual_projects_watcher_list = []
    for project in data:
        if watcher in project['watchers']:
            project_dict = {'project': {'name': project['name'], 'priority': project['priority']}}
            individual_projects_watcher_list.append(project_dict)
    individual_projects_watcher_list = sorted(individual_projects_watcher_list, key=lambda k: k['project']['priority'])
    all_projects_watchers_list.append(individual_projects_watcher_list)

all_only_name_projects_managers = []
for x in range(len(all_projects_managers_list)):
    individual_only_name_projects = []
    obj = all_projects_managers_list[x]
    for y in obj:
        individual_only_name_projects.append(y['project']['name'])
    all_only_name_projects_managers.append(individual_only_name_projects)

new_data_managers = {}
loop_counter_managers = 0
for manager in managers_list:
    new_data_managers.update({manager: all_only_name_projects_managers[loop_counter_managers]})
    loop_counter_managers += 1

all_only_name_projects_watchers = []
for x in range(len(all_projects_watchers_list)):
    individual_only_name_projects = []
    obj = all_projects_watchers_list[x]
    for y in obj:
        individual_only_name_projects.append(y['project']['name'])
    all_only_name_projects_watchers.append(individual_only_name_projects)

new_data_watchers = {}
loop_counter_watchers = 0
for watcher in watchers_list:
    new_data_watchers.update({watcher: all_only_name_projects_watchers[loop_counter_watchers]})
    loop_counter_watchers += 1
        
with open('managers.json', 'w') as f:
    json.dump(new_data_managers, f, indent=2)

with open('watchers.json', 'w') as f:
    json.dump(new_data_watchers, f, indent=2)