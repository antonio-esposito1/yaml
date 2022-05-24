#!/usr/bin/python3.9

if __name__== "__main__":
 import yaml
 with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)
 user = data['user']
 print(user['name'])
 for role in user['roles']:
    print(role)
 user['location']['city'] = ['Dallas']
 with open('yaml_example-edit.yml', 'w') as file:
    yaml.dump(data,file, default_flow_style=False)