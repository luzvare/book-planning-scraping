'use strict';

const fs = require('fs');

let data = fs.readFileSync('book_data.csv', 'utf-8');
data = data.replaceAll(',,,,,,\n', '')
console.log(data);
fs.writeFileSync('book_data_formated.csv', data, 'utf-8');