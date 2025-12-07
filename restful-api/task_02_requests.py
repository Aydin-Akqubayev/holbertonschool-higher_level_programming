#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        for i in data:
            print(i.get('title'))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        fieldname = ['id', 'title', 'body']
        filter_json = []
        res = {}
        for i in data:
            res['id'] = i.get('id')
            res['title'] = i.get('title')
            res['body'] = i.get('body')
            filter_json.append(res)
            res = {}
        with open("posts.csv", 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldname)
            writer.writeheader()
            writer.writerows(filter_json)
