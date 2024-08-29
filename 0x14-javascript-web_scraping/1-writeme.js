#!/usr/bin/node
// read and print 


const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  else
  console.log(data)
});
