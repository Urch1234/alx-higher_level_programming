#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (!size) {
	console.log('Missing size');
} else {
	for (let i = 0; i < size; i++) {
		for (j = 0; j < size; j++) {
			console.log('X');
		}
		console.log('');
	}
}
