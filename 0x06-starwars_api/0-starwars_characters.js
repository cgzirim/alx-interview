#!/usr/bin/node

if (process.argv.length > 2) {
  const id = process.argv[2];
  const request = require('request');
  const API_URL = 'https://swapi-api.hbtn.io/api/films/' + id;

  request(API_URL, (err, resp, body) => {
    if (err) console.log(err);
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, resp, body) => {
          if (err) reject(err);

          resolve(JSON.parse(body).name);
        });
      }));
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
