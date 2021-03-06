"use strict";

const fs = require("fs");
const _ = require("lodash");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", inputStdin => {
  inputString += inputStdin;
});

process.stdin.on("end", _ => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map(str => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the countingValleys function below.
function countingValleys(numberOfSteps, steps) {
  let altitude = 0;
  let enteringValley = 0;
  steps.split("").forEach(step => {
    if (isEnteringValley(step, altitude)) {
      enteringValley += 1;
    }
    if (isDownhill(step)) {
      altitude -= 1;
    } else if (isUphill(step)) {
      altitude += 1;
    }
  });
  return enteringValley;
}

function isEnteringValley(step, altitude) {
  return isDownhill(step) && isAtSeaLevel(altitude);
}

function isAtSeaLevel(altitude) {
  return altitude === 0;
}

function isDownhill(step) {
  return step === "D";
}

function isUphill(step) {
  return step === "U";
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const numberOfSteps = parseInt(readLine(), 10);

  const path = readLine();

  let result = countingValleys(numberOfSteps, path);

  ws.write(result + "\n");

  ws.end();
}
