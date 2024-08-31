#!/usr/bin/node
// print

const rq = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body).characters;
  for (let i = 0; i < data.length; i++) {
    rq(data[i], (err, resp, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
