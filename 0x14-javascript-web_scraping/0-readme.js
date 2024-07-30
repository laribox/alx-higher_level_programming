#!/usr/bin/node
const file_name = process.argv[2];
const fs = require('fs');
fs.readFile(file_name, 'utf-8', (error, data) => {
	  if (error) {
		      console.error(error);
		      return;
		    }
	  console.log(data);
});
