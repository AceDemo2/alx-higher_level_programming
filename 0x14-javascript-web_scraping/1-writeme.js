#!/usr/bin/node
// read and print 


const fs = require('fs');
fs.writeFile(process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
