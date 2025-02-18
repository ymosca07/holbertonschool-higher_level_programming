import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(f"Status Code: {response.status_code}")

        posts = response.json()
        for post in posts:
            print(post["title"])

    except requests.exceptions.RequestException as e:
        print(f"Status Code Error: : {e}")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        response.raise_for_status()

        posts = response.json()

        fieldnames = ["id", "title", "body"]
        filtered_posts = [{key: post[key] for key in fieldnames}
                          for post in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_posts)

        print("✅ Données enregistrées dans posts.csv")

    except requests.exceptions.RequestException as e:
        print(f"Status Code Error: {e}")
