import json
import csv

SCHEMA = {
    "title": "Floor Access Event",
    "type": "object",
    "properties": {
        "person_id": {
            "type": "string"
        },
        "datetime": {
            "type": "string",
            "format": "date-time"
        },
        "floor_level": {
            "type": "integer"
        },
        "building": {
            "type": "string"
        }
    },
    "required": ["person_id", "datetime", "floor_level", "building"]
}

def main():
    with open("questao_01.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_data = [
                        row["Person Id"],
                        row["Floor Access DateTime"],
                        row["Floor Level"],
                        row["Building"],
                    ]
            json_obj = serialize(row_data)





def serialize(arr):
    data =  SCHEMA.copy()
    data["required"][0] = arr[0] 
    data["required"][1] = arr[1]
    data["required"][2] = int(arr[2])
    data["required"][3] = arr[3]
    
    return json.dumps(data)

if __name__ == "__main__":
    main()
