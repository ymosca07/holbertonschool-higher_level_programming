import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}")
    else:
        print(response.status_code)


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    fieldnames = ['id', 'title', 'body']
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
    else:
        print(response.status_code)
