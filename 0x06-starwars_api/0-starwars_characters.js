#!/usr/bin/node

if (process.argv.length > 2) {
  const id = process.argv[2];
  const request = require('request');
  const API_URL = 'https://swapi-api.hbtn.io/api/films/' + id;

  request(API_URL, (err, resp, body) => {
    if (err) console.log(err);
    const charactersURL = JSON.parse(body).characters;

    for (let i = 0; i < charactersURL.length; i++) {
      request(charactersURL[i], (err, resp, body) => {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
      });
    }
  });
}
