import json

def write_tofile(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)