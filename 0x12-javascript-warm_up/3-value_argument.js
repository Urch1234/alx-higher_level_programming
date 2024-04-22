#!/usr/bin/node
  2 /*
  3  * a script that prints the first argument passed to it
  4  * If no arguments are passed to the script, print “No argument”
  5  * If no arguments are passed to the script, print “No argument”
  6  */
  const args = process.argv[2];
  if (args === undefined) {
    console.log('No argument');
 } else {
    console.log(args);
 }
