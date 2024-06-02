import requests
import gzip
import json
import random

# url of file to download
url = "https://production-media.paperswithcode.com/about/links-between-papers-and-code.json.gz"
response = requests.get(url, stream=True)

# download the file
with open("links-between-papers-and-code.json.gz", mode="wb") as file:
    for chunk in response.iter_content(chunk_size=10 * 1024):
        file.write(chunk)

# opening and decoding
with gzip.open("links-between-papers-and-code.json.gz", "rb") as f:
    data = json.loads(f.read().decode("utf-8"))

input('Hit enter to load a paper')

is_done = False
while not is_done:
    # get a random listing number
    rand_listing = random.randint(0, len(data)-1)

    # print(data[rand_listing])
    # print(data[rand_listing]['paper_url'])
    print()
    print("title: " + data[rand_listing]['paper_title'])
    print("pdf: " + data[rand_listing]['paper_url_pdf'])
    print("repo: " + data[rand_listing]['repo_url'] + "\n")

    done_question = input('Load another listing? (y/n)')
    if done_question == 'n':
        is_done = True
