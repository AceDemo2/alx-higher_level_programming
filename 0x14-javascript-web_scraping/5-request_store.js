#!/usr/bin/node
//store content

const fs = require('fs');
const rq = require('request');
const api = process.argv[2];
const file = process.argv[3];
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
