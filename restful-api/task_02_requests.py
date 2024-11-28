""" This module fetches posts from the API and prints them to the console """
import csv
import requests



def fetch_and_print_posts():
    """ Fetches posts from the API and prints them to the console """

    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url, timeout=10)
    posts = response.json()
    print("Status Code: ", response.status_code)    
    for post in posts:
        print(post["title"])

    # requests.post(api_url, data={"UserId": 1, "title": "John", "completed": false})
    #requests.put(api_url, data={"key": "value"})
    #requests.delete(api_url)


    # print(response.headers["Content-Type"])

def fetch_and_save_posts():
    """ Fetches posts from the API and saves them to a CSV file """

    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url, timeout=10)
    posts = response.json()
    diclist = []
    for post in posts:
        diclist.append({"userId": post["userId"], "title": post["title"], "body": post["body"]})
        print(post["title"])
    with open("posts.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["userId", "title", "body"])
        writer.writeheader()
        for dic in diclist:
            writer.writerow(dic)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()