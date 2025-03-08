import json

def update_json_value(file_path, key, value):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        data[key] = value
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except:
        return Exception


