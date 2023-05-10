import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

    
titles = []
ratings = []
rating_and_review_numbers = []
prices = []
mrps = []
asns = []
links = []
brands = []
pages = []
product_ranks = []
images = []
type = int(input("Enter 1 for url and 2 for asn: "))
if type == 1:
    url1 = input("Enter url ")
    page = int(input("Enter no of pages "))
    for x in range(1, page + 1):
        url = url1 + f"&page={x}"
        response = requests.get(url)
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")

        elements = soup.find_all("div", {"class": "_1xHGtK _373qXS"})
        elements1 = soup.find_all("div", {"class": "_13oc-S"})
        count = 0
        if elements:
            first_part = "https://www.flipkart.com"
            for i in range(len(elements)):
                sec_part = elements[i].find("a").get("href")
                final_url = first_part + sec_part
                links.append(final_url)

                response = requests.get(final_url)
                page_content = response.text
                soup = BeautifulSoup(page_content, "html.parser")
                print(final_url)
                count += 1

                pages.append(x)
                product_ranks.append(count)

                title_soup = soup.find("div", class_="aMaAEs")
                if title_soup:
                    title = title_soup.find("span", class_="B_NuCI")

                    if title:
                        title = title.text
                        titles.append(title)
                    else:
                        title = ""
                        titles.append(title)
                    rating = title_soup.find("div", class_="_3LWZlK")
                    if rating:
                        rating = rating.text
                        ratings.append(rating)
                    else:
                        ratings.append("")
                    rating_and_review_soup = title_soup.find("span", class_="_2_R_DZ")
                    if rating_and_review_soup:
                        rating_and_review = rating_and_review_soup.text.split(
                            " Ratings"
                        )[0]
                        rating_and_review_numbers.append(rating_and_review)
                    else:
                        rating_and_review_numbers.append("")

                else:
                    titles.append("")
                    ratings.append("")
                    rating_and_review_numbers.append("")

                price_soup = soup.find("div", class_="_30jeq3 _16Jk6d")

                if price_soup:
                    price = price_soup.text.replace("₹", "")
                    prices.append(price)

                else:
                    prices.append("")

                description = soup.find(class_="_3dtsli")
                if description:
                    split = description.text.split("Brand")
                    if len(split) > 1:
                        brand = split[1].split("Model")[0]
                        brands.append(brand)
                    else:
                        brand = ""
                        brands.append(brand)
                else:
                    brands.append("")

                mrp_soup = soup.find("div", class_="_3I9_wc _2p6lqe")
                if mrp_soup:
                    mrp = mrp_soup.text.replace("₹", "")
                    mrps.append(mrp)
                else:
                    mrps.append("")
                asn = final_url.split("pid=")[1].split("&")[0]
                asns.append(asn)

                image_soup = soup.find("div", {"class": "CXW8mj _3nMexc"})
                if image_soup:
                    image1 = image_soup.find("img")
                    image = image1.get("src")
                    images.append(image)
                else:
                    images.append("")

            data = {
                "page": pages,
                "Product_rank": product_ranks,
                "Asn": asns,
                "titles": titles,
                "price": prices,
                "rating": ratings,
                "no_of_rating": rating_and_review_numbers,
                "mrp": mrps,
                "price": prices,
                "brand": brands,
                "links": links,
                "image": images,
            }
            df = pd.DataFrame(data)
            df.to_csv("output.csv")
        elif elements1:
            first_part = "https://www.flipkart.com"
            count = 0
            for k in range(len(elements1)):
                link_group = elements1[k].find_all("a")

                for j in range(len(link_group)):
                    if j % 3 == 0:
                        final_url = first_part + link_group[j].get("href")

                        response = requests.get(final_url)
                        page_content = response.text
                        soup = BeautifulSoup(page_content, "html.parser")
                        print(final_url)
                        links.append(final_url)

                        count += 1

                        pages.append(x)
                        product_ranks.append(count)

                        title_soup = soup.find("div", class_="aMaAEs")
                        if title_soup:
                            title = title_soup.find("span", class_="B_NuCI")

                            if title:
                                title = title.text
                                titles.append(title)
                            else:
                                title = ""
                                titles.append(title)
                            rating = title_soup.find("div", class_="_3LWZlK")
                            if rating:
                                rating = rating.text
                                ratings.append(rating)
                            else:
                                ratings.append("")
                            rating_and_review_soup = title_soup.find(
                                "span", class_="_2_R_DZ"
                            )
                            if rating_and_review_soup:
                                rating_and_review = rating_and_review_soup.text.split(
                                    " Ratings"
                                )[0]
                                rating_and_review_numbers.append(rating_and_review)
                            else:
                                rating_and_review_numbers.append("")

                        else:
                            titles.append("")
                            ratings.append("")
                            rating_and_review_numbers.append("")

                        price_soup = soup.find("div", class_="_30jeq3 _16Jk6d")

                        if price_soup:
                            price = price_soup.text.replace("₹", "")
                            prices.append(price)

                        else:
                            prices.append("")

                        description = soup.find(class_="_3dtsli")
                        if description:
                            split = description.text.split("Brand")
                            if len(split) > 1:
                                brand = split[1].split("Model")[0]
                                brands.append(brand)
                            else:
                                brand = ""
                                brands.append(brand)
                        else:
                            brands.append("")

                        mrp_soup = soup.find("div", class_="_3I9_wc _2p6lqe")
                        if mrp_soup:
                            mrp = mrp_soup.text.replace("₹", "")
                            mrps.append(mrp)
                        else:
                            mrps.append("")
                        asn = final_url.split("pid=")[1].split("&")[0]
                        asns.append(asn)

                        image_soup = soup.find("div", {"class": "CXW8mj _3nMexc"})
                        if image_soup:
                            image1 = image_soup.find("img")
                            image = image1.get("src")
                            images.append(image)
                        else:
                            images.append("")
            data = {
                "page": pages,
                "Product_rank": product_ranks,
                "Asn": asns,
                "titles": titles,
                "price": prices,
                "rating": ratings,
                "no_of_rating": rating_and_review_numbers,
                "mrp": mrps,
                "price": prices,
                "brand": brands,
                "links": links,
                "image": images,
            }
            df = pd.DataFrame(data)
            df.to_csv("output.csv")
else:
    import csv

    file_name = "asn.csv"

    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url = f"https://www.flipkart.com/raegr-rg10451-arc-one-15w-type-c-pd-made-india-qi-enabled-wireless-charger-charging-pad/p/itme8b1434aacf1d?pid={row[0]}"

            response = requests.get(url)
            final_url = url
            page_content = response.text
            soup = BeautifulSoup(page_content, "html.parser")
            print(final_url)
            links.append(final_url)

            title_soup = soup.find("div", class_="aMaAEs")
            if title_soup:
                title = title_soup.find("span", class_="B_NuCI")

                if title:
                    title = title.text
                    titles.append(title)
                else:
                    title = ""
                    titles.append(title)
                rating = title_soup.find("div", class_="_3LWZlK")
                if rating:
                    rating = rating.text
                    ratings.append(rating)
                else:
                    ratings.append("")
                rating_and_review_soup = title_soup.find("span", class_="_2_R_DZ")
                if rating_and_review_soup:
                    rating_and_review = rating_and_review_soup.text.split(" Ratings")[0]
                    rating_and_review_numbers.append(rating_and_review)
                else:
                    rating_and_review_numbers.append("")

            else:
                titles.append("")
                ratings.append("")
                rating_and_review_numbers.append("")

            price_soup = soup.find("div", class_="_30jeq3 _16Jk6d")

            if price_soup:
                price = price_soup.text.replace("₹", "")
                prices.append(price)

            else:
                prices.append("")

            description = soup.find(class_="_3dtsli")
            if description:
                split = description.text.split("Brand")
                if len(split) > 1:
                    brand = split[1].split("Model")[0]
                    brands.append(brand)
                else:
                    brand = ""
                    brands.append(brand)
            else:
                brands.append("")

            mrp_soup = soup.find("div", class_="_3I9_wc _2p6lqe")
            if mrp_soup:
                mrp = mrp_soup.text.replace("₹", "")
                mrps.append(mrp)
            else:
                mrps.append("")
            asn = final_url.split("pid=")[1].split("&")[0]
            asns.append(asn)

            image_soup = soup.find("div", {"class": "CXW8mj _3nMexc"})
            if image_soup:
                image1 = image_soup.find("img")
                image = image1.get("src")
                images.append(image)
            else:
                images.append("")
    data = {
        "Asn": asns,
        "titles": titles,
        "price": prices,
        "rating": ratings,
        "no_of_rating": rating_and_review_numbers,
        "mrp": mrps,
        "price": prices,
        "brand": brands,
        "links": links,
        "image": images,
    }
    df = pd.DataFrame(data)
    df.to_csv("output.csv")
