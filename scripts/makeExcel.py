from json import loads, load
from csv import DictWriter

def get_json_content(filepath):
    with open(filepath) as json_file:
        data = load(json_file)
    return data

def get_type(value):
    if value == str:
        return "String"
    elif value == int:
        return "Integer"
    elif value == float:
        return "Float"
    elif value == list:
        return "Array"
    elif value == dict:
        return "Dictionary"
    else:
        return "error"

def make_csv_file(data, output_path):
    with open(output_path, "w", newline= "") as csvfile:
        fieldnames = ["path","example","type"]
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({
                "path": item[0], 
                "example": item[1], 
                "type": get_type(item[2])})

def json_to_excel(filepath, output_path = "files/output.csv"):
    data = get_json_content(filepath)

    data = verify_json_node(None, data)
    
    make_csv_file(data, output_path)


def verify_json_node(key_name, json_data, resultArray = []):
    key_str = key_name + " - > " if key_name is not None else ""
    if type(json_data) is dict:
        for key, value in json_data.items():
            # print(key)
            verify_json_node(f'{key_str}{key}', value, resultArray)
    elif type(json_data) is list:
        cont_number = 0
        for item in json_data:
            verify_json_node(key_name+f"[{cont_number}]", item, resultArray)
            cont_number +=1
    else:
        resultArray.append([key_name, json_data, type(json_data)])
        # print(resultArray)
    return resultArray

json_to_excel("files/input.json")
