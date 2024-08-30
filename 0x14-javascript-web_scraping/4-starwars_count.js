#!/usr/bin/node
// starwars_title.js

const rq = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
rq(api, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  const numberFilm = data.results.length;

  for (let i = 0; i < numberFilm; i++) {
    const numberCharacters = data.results[i].characters.length;

    for (let j = 0; j < numberCharacters; j++) {
      const filmForCharacter = data.results[i].characters[j];

      if (filmForCharacter.includes('18') === true) {
        count += 1;
      }
    }
  }
  console.log(count);
});
