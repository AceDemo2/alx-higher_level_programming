#!/usr/bin/node
// record

const rq = require('request');
const api = process.argv[2];
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const store = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      if (!store[data[i].userId]) {
        store[data[i].userId] = 1;
      } else {
        store[data[i].userId]++;
      }
    }
  }
  console.log(store);
});
