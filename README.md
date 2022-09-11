# Web Scraping for books

- TFG - Full Stack project
- Luciana Belén Varela Díaz

In this repository is the source code to the web-scraping for amazon. The main goal is to search for a type of books on amazon, and our web scraping bot is going to get all the information we need.

## How to perform the web scraping

We have three main python programs. It is necessary to have python installed in our computer. The order is as follows.

### get-books-pages.py

This program is in charge of performing a search on amazon. When we call the function `search_amazon()` we pass what we want to search. For example, at the moment we are searching for "Libros de fantasía".

If this runs correctly, we will have a new file named `search_results_urls.txt`. With a list of pages to search for books.

### get-books-from-pages.py

In this program we open the previously generated file, we open each page and extract all the books from that page, getting the detail url of each one of them. And storing that url on another file called `new_search_results.txt`.

### get-books-info.py

This is the main part of the web scraping, once we have collected all the books, we open each url and extract the information we need.

We are collecting the following data:

- Name
- Author
- ISBN-10
- ISBN-13
- Editorial
- Pages
- Image

All that information is stored on our `book_data.csv`.

### Format and database storage

#### Format

Once we have the data in csv format, we are going to convert that to a JSON file. In order to do so we execute `csv-to-json.py`. This is going to generate a new file, named `bookData.json`. This file is going to be used to store our newly scrapped books in our database.

#### Database

To store in our local database we have to execute the file `add-to-database.js`, this program is going to read our json, take the books that have at least one ISBN stored and call our API to search for the rest of the information and save that in our database.
