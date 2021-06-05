import requests
import json


def repository_language_iterator():
    o = 0
    l = []
    for i in requests.get("https://api.github.com/users/thekaigonzalez/repos").json():
        l.append(requests.get("https://api.github.com/users/thekaigonzalez/repos").json()[o]['language'])
        o += 1
    return l

print(repository_language_iterator())