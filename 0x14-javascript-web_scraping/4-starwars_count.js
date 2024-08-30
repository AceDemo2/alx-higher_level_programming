#!/usr/bin/node
// starwars_title.js

const rq = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  let count = 0;
  const reslen = data.results.length;
  for (let i = 0; i < reslen; i++) {
    const charlen = data.result[i].characters.length;
    for (let j = 0; j < charlen; j++) {
      const charsplit = characters[j].split('/')[5];
      if (charsplit === '18') { count += 1; }
    }
  }
  console.log(count);
});
