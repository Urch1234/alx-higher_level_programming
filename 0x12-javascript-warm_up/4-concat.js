#!/usr/bin/node
/*
 * A script that prints two arguments passed to it
 * Using console.log(...) to print all output.
 * var not allowed
 */
const args = process.argv.length;

if (args === 3) {
	console.log(`${args[2]} is ${args[3]}`);
} else if (args === 2) {
	console.log(`${args[2]} is undefined`);
} else {
	console.log('undefined is undefined');
}
