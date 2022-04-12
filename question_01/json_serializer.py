import json

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
    pass

def serialize(arr):
    data =  SCHEMA.copy()
    data["required"][0] = arr[0] 
    data["required"][1] = arr[1]
    data["required"][2] = int(arr[2])
    data["required"][3] = arr[3]
    
    return json.dumps(data)

if __name__ == "__main__":
    main()
