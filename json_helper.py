import json


def read_json(file_path):
    json_open = open(file_path)
    json_object = json.load(json_open)
    return json_object

print(read_json('/Users/joe/PycharmProjects/Python9Ex/data/super_smash_bros/link.json'))
