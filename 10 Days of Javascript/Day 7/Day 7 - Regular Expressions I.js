"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function regexVar() {
  /*
   * Declare a RegExp object variable named 're'
   * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
   */

  let re = /^(a|e|i|o|u).*\1$/;

  //  ^ => first item matches.
  // () => stores matching value captured within
  // (a|e|i|o|u)=> matches any of the characters in the brackets
  // . => matches any character.
  // * => for 0,1 or more occurrances (this ensures str length > 3)
  // \1 => matches to previously stored match.

  /*
   * Do not remove the return statement
   */
  return re;
}

function main() {
  const re = regexVar();
  const s = readLine();

  console.log(re.test(s));
}
