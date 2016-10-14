ivan = {
    "name": "ivan",
    "age": 34,
    "children":[{
        "name": "vasja",
        "age":12,
    },{
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    },{
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]

def more_then_18(arr):
    a = []
    for el in arr:
        for child in el['children']:
            if child['age'] > 18:
                a.append(el['name'])
                break
    return a

print("Искомые сотрудники:", more_then_18(emps))