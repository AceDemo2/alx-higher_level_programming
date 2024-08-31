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

  print(data, 0);
});
function print (data, ind) {
  if (ind === data.length) {
    return;
  }
  rq(data[ind], (err, resp, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const name = JSON.parse(body).name;
    console.log(name);
    print(data, ind + 1);
  });
}
