#!/usr/bin/node

const request = required('request');
const url = process.argv[2];

request.get(url, (error, response) => {
				if (error) {
								console.log(error);
				} else {
								console.log(`code: ${response.statuscode}`);
				}
});
