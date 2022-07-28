#!/usr/bin/node

const id = process.argv[2];

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, (err, resp, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (err, resp, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
});
