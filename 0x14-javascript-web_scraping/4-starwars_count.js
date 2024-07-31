#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body).results;
  data.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(18)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
