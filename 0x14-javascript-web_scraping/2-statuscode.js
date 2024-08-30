#!/usr/bin/node
// get

const rq = require('request');
rq(process.argv[2], (err, resp) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ', resp.statusCode);
});
