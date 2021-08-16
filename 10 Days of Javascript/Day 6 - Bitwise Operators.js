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

// ========================
//         Solution
// ========================

function getMaxLessThanK(n, k) {
  let maxi = 0;
  let curr = -1;

  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j <= n; j++) {
      curr = i & j;
      if (curr < k && curr > maxi) {
        maxi = curr;
      }
    }
  }
  return maxi;
}

function main() {
  const q = +readLine();

  for (let i = 0; i < q; i++) {
    const [n, k] = readLine().split(" ").map(Number);

    console.log(getMaxLessThanK(n, k));
  }
}
