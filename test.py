import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9\-\_\.]", "", new_id)
    new_id = re.sub("\.+", ".", new_id)
    new_id = re.sub("(^\.)|(\.$)", "", new_id)
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub("(^\.)|(&\.)", "", new_id)
    id_len = len(new_id)
    if id_len <= 2:
        new_id += new_id[-1] * (3 - id_len) 
    
    return new_id


print(solution("z-+.^."))