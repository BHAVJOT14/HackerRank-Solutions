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

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
  const vowel = [];
  const consonant = [];

  for (let i = 0; i < s.length; i++) {
    if (
      s[i] == "a" ||
      s[i] == "e" ||
      s[i] == "i" ||
      s[i] == "o" ||
      s[i] == "u"
    ) {
      vowel.push(s[i]);
    } else {
      consonant.push(s[i]);
    }
  }

  //  Below this for loop will help to print
  //  the vowels & consonants in new line

  for (let x in vowel) {
    console.log(vowel[x]);
  }
  for (let x in consonant) {
    console.log(consonant[x]);
  }
}

function main() {
  const s = readLine();

  vowelsAndConsonants(s);
}
