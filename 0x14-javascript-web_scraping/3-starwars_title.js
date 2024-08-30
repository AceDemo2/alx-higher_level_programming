#!/usr/bin/node
// starwars_title.js

const rq = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
