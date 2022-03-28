import json
import os
import pickle


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

def write_pickle(file_path):
    pickle_file = open('pickle_file', 'wb')
    pickle.dump(file_path, pickle_file)

def load_pickle(file_path):
    load_file = open(path, 'rb')
    return pickle.load(load_file)

