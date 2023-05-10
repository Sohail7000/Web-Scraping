import requests
from bs4 import BeautifulSoup

type = int(input("Enter 1 for url and 2 for asn"))

if type == 1:
    url1 = input("Enter url")
    page = int(input("Enter number of pages"))

    for x in range(1, page + 1):
        url = url1 + f"&page={x}"
        response = requests.get(url)
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")

        elements = soup.find_all("a", {"class": "_1fQZEK"})
        # the element list has stored a list with all the elements with a tag
        print(elements)

        if elements:
            first_part = "https://www.flipkart.com"
            # for i in range(len(element)):
            sec_part = elements[1].find("a").get("href")

            print(sec_part)
