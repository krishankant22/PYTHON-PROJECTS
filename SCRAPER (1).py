import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

try:
    # Send request to website
    response = requests.get(url)

    # Check connection status
    if response.status_code == 200:
        print("Website connected successfully!")
    else:
        print(f"Failed to connect. Status code: {response.status_code}")

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Empty list to store book data
    books_data = []

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Extract data from each book
    for book in books:

        # Book title
        title = book.h3.a["title"]

        # Book price
        price = book.find("p", class_="price_color").text

        # Book rating
        rating = book.p["class"][1]

        # Store extracted data
        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

    # Convert data into dataframe
    df = pd.DataFrame(books_data)

    # Save dataframe into CSV file
    df.to_csv("books_data.csv", index=False, encoding="utf-8")

    print("Data saved successfully in books_data.csv")

except Exception as e:
    print("An error occurred:", e)
