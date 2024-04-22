#!/usr/bin/node
/*
 * a script that prints the first argument passed to it
 * If no arguments are passed to the script, print “No argument”
 * If no arguments are passed to the script, print “No argument”
 */
const args = process.argv[2];
if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
