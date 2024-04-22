#!/usr/bin/node
/*
 * A script that prints two arguments passed to it
 * Using console.log(...) to print all output.
 * var not allowed
 */
const argv0 = process.argv[2]
const argv1 = process.argv[3]

console.log(`${argv0} is ${argv1}`);
