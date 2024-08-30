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
  let reslen = data.result.length
  for (let i = 0; i < reslen; i++) {
    let 
    for (let j = 0; j < result[j]; j++) {
        let charlen = result[j].character.length
	for (let k = 0; k < charlen; k++) {
  forEach
	console.log(data.title);
});
