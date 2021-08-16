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

function getLetter(s) {
  let letter;
  // Write your code here
  let array_1 = ["a", "e", "i", "o", "u"];
  let array_2 = ["b", "c", "d", "f", "g"];
  let array_3 = ["h", "j", "k", "l", "m"];
  let array_4 = ["n", "p", "q", "r", "s", "t", "v", "x", "y", "z"];

  switch (true) {
    case array_1.includes(s.charAt(0)):
      return "A";
      break;
    case array_2.includes(s.charAt(0)):
      return "B";
      break;
    case array_3.includes(s.charAt(0)):
      return "C";
      break;
    case array_4.includes(s.charAt(0)):
      return "D";
      break;
    default:
      break;
  }
  return letter;
}

function main() {
  const s = readLine();

  console.log(getLetter(s));
}
