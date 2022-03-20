import json
import os


def read_json(file_path):
    json_open = open(file_path)
    json_object = json.load(json_open)
    return json_object

def read_all_json_files(file_path):
    all_json_files = []
    for file in os.listdir(file_path):
        full_filename = '%s%s' % (file_path, file)
        with open(full_filename, 'r') as f:
            temp_dict = json.load(f)
            all_json_files.append(temp_dict)

    return all_json_files

print(read_all_json_files('/Users/joe/PycharmProjects/Python9Ex/data/super_smash_bros/'))
