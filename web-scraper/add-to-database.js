"use strict";

import axios from "axios";
import fs from "fs";

let data = fs.readFileSync("bookData.json", "utf-8");
let jsonData = JSON.parse(data);
let parsedJsonData = [];
jsonData.forEach((element) => {
  if (element["ISBN-10"] != "" || element["ISBN-13"] != "") {
    parsedJsonData.push({
      ...element,
    });
  }
});
async function addBook(googleId, bookData) {
  return await axios
    .post("http://localhost:3000/books", {
      googleId: googleId,
      bookData: bookData,
    })
    .then((data) => data.data);
}
async function searchBook(isbn) {
  return await axios
    .get(`http://localhost:3000/search?isbn=${isbn}`)
    .then((data) => data.data);
}

async function searchAndSaveBook(isbn) {
  const result = await searchBook(isbn);
  if (result["items"] != undefined && result["items"].length > 0) {
    const book = result["items"][0];
    const addResponse = await addBook(book["id"], book);
    console.log(addResponse);
  }
}

async function getAllBooks() {
  for (let amazonBook = 0; amazonBook < 20; amazonBook++) {
    if (parsedJsonData[amazonBook]["ISBN-10"] != "") {
      await searchAndSaveBook(parsedJsonData[amazonBook]["ISBN-10"]);
    } else if (parsedJsonData[amazonBook]["ISBN-13"] != "") {
      await searchAndSaveBook(parsedJsonData[amazonBook]["ISBN-13"]);
    }
  }
}

getAllBooks();
