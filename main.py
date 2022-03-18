import json
from xmlrpc.client import Boolean, boolean
import jsonschema
from jsonschema import validate

schema1 = { 
               "type": "object",
               "properties": {
                 "AppName": {"type": "string"},
                 "EventType": {"type": "string"},
                 "subEventType":{"type":"string"},
                "tag":  {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
}


def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=schema1)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData = {"AppName":"", "eventType":"", "tag": "", "subEventType":"", "description": "", "required": "False"}
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

schema2 = { 
               "type": "object",
               "properties": {
                "id": {"type": "string" },
                "name": {"type":"string"},
                "orientation": {"type":"string"},
                "tag":  {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson1(jsonData1):
    try:
        validate(instance=jsonData1, schema=schema2)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData1 = {"id": "", "name":"", "orientation":"", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson1(jsonData1)
if isValid:
    print(jsonData1)
    print("Given JSON data is Valid")
else:
    print(jsonData1)
    print("Given JSON data is InValid")

schema3 = { 
               "type": "object",
               "properties": {
                "minParticipants": {"type": "number"},
                "maxParticipants": {"type": "number"},
                "battleType": {"type":"string"},
                "WagerType": {"type":"string"},
                "countdown": {"type": "number"},
                "duration": {"type": "number"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson2(jsonData2):
    try:
        validate(instance=jsonData2, schema=schema3)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData2 = {"minParticipants": 942, "maxParticipants": 641, "battleType": "ABCDEFGHIJKLMN","wagerType": "ABCDEFGHIJKLMNOPQRSTUVW","countdown": 69,"duration": 200, "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData2)
if isValid:
    print(jsonData2)
    print("Given JSON data is Valid")
else:
    print(jsonData2)
    print("Given JSON data is InValid")


schema4 = { 
               "type": "object",
               "properties": {
                "name": {"type": "string"},
                "IconId": {"type":"string"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson3(jsonData3):
    try:
        validate(instance=jsonData3, schema=schema4)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData3 = {"name":"", "iConId":"", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData3)
if isValid:
    print(jsonData3)
    print("Given JSON data is Valid")
else:
    print(jsonData3)
    print("Given JSON data is InValid")

schema5 = { 
               "type": "object",
               "properties": {
                "status": {"type": "string"},
                "creationTime": {"type": "number"},
                "startTime": {"type": "number"},
                 "endTime": {"type": "number"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson4(jsonData4):
    try:
        validate(instance=jsonData4, schema=schema5)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData4 = {"status": "ABCDEFGHIJKL","creationTime": 240,"startTime": 626,"endTime": 353, "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData4)
if isValid:
    print(jsonData4)
    print("Given JSON data is Valid")
else:
    print(jsonData4)
    print("Given JSON data is InValid")


schema6 = { 
               "type": "object",
               "properties": {
               "id": {"type": "string"},
               "nickname": {"type": "string"},
               "title": {"type": "string"},
               "accountType": {"type": "string"},
               "countryCode": {"type": "string"},
               "orientation": {"type": "string"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson5(jsonData5):
    try:
        validate(instance=jsonData5, schema=schema6)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData5 = {"id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA", "nickname": "ABCDEFGHIJKLMNOPQ", "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "accountType": "ABCDE", "countryCode": "ABCD", "orientation": "ABCDEFGHIJKLMNO", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData5)
if isValid:
    print(jsonData5)
    print("Given JSON data is Valid")
else:
    print(jsonData5)
    print("Given JSON data is InValid")
schema7 = { 
               "type": "object",
               "properties": {
               "id": {"type": "string"},
               "nickname": {"type": "string"},
               "title": {"type": "string"},
               "accountType": {"type": "string"},
               "countryCode": {"type": "string"},
               "orientation": {"type": "string"},
                "tag": {"type": "number"},
                "description": {"type": "number"}

               },
               "required": [],
} 

def validateJson6(jsonData6):
    try:
        validate(instance=jsonData6, schema=schema7)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData6 = { "id": "ABCDEFGHIJKLMN", "nickname": "ABCDEFGHIJKLMN", "title": "ABCDEFGHIJK", "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX", "countryCode": "ABCDEFGH","orientation": "ABCDEFGHIJKLMNOPQRSTUVWXY", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData6)
if isValid:
    print(jsonData6)
    print("Given JSON data is Valid")
else:
    print(jsonData6)
    print("Given JSON data is InValid")

schema8 = { 
               "type": "object",
               "properties": {
               "ranking": {"type": "number"},
               "numberOfTrades": {"type": "number"},
               "performance": {"type": "string"}, 
                "name": {"type": "string"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson7(jsonData7):
    try:
        validate(instance=jsonData7, schema=schema8)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData7 = {"ranking": 498,"numberOfTrades": 862, "performance": "ABCDEFGHIJKLMNOPQRSTUVW", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData7)
if isValid:
    print(jsonData7)
    print("Given JSON data is Valid")
else:
    print(jsonData7)
    print("Given JSON data is InValid")


schema9 = { 
               "type": "object",
               "properties": {
               "id": {"type": "string"},
               "nickame": {"type": "string"},
               "title": {"type": "string"}, 
                "accountType": {"type": "string"},
                "orientation": {"type": "string"},
                "countryCode": {"type": "string"},
                "tag": {"type": "string"},
                "description": {"type": "string"}

               },
               "required": [],
} 

def validateJson8(jsonData8):
    try:
        validate(instance=jsonData8, schema=schema9)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData8 = { "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB", "nickname": "ABCDEFGHIJKLMNO", "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC", "accountType": "ABCDEFGHIJKLMNOPQRS", "countryCode": "ABCDEFGHIJKLMNOPQR", "orientation": "ABCDEFGHIJKLMNOPQR", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData8)
if isValid:
    print(jsonData8)
    print("Given JSON data is Valid")
else:
    print(jsonData8)
    print("Given JSON data is InValid")

with open("schema/schema_1.json", "w") as f:
    json.dump(schema9, f)


schema10 = { 
               "type": "object",
               "properties": { 
                "name":[],
                "tag": {"type": "string"},
                "description": {"type": "string"}
               },
               "required": [],
} 

def validateJson9(jsonData9):
    try:
        validate(instance=jsonData9, schema=schema10)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData9 = { "name":"", "tag": "", "description": "", "required": "False"}
# validate it
isValid = validateJson2(jsonData9)
if isValid:
    print(jsonData9)
    print("Given JSON data is Valid")
else:
    print(jsonData9)
    print("Given JSON data is InValid")

with open("schema/schema_1.json", "w") as outfile:
    json.dump(schema10, outfile)