function trimWhitespace(data) {
  return data.trim();
}

function splitByComma(str) {
  return str.split(",");
}

function convertToNumbers(arr) {
  return arr.map((item) => parseInt(item));
}

function filterEvenNumbers(nums) {
  return nums.filter((num) => num % 2 === 0);
}

function processData(data) {
  const cleaned = trimWhitespace(data);
  const parts = splitByComma(cleaned);
  const nums = convertToNumbers(parts);
  return filterEvenNumbers(nums);
}

function processData(data) {
  // trim whitespace
  let cleaned = data.trim();
  // split by comma
  const parts = cleaned.split(",");
  // convert to numbers
  const nums = [];
  for (let i = 0; i < parts.length; i++) {
    nums.push(parseInt(parts[i]));
  }
  // filter even numbers
  const evens = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 === 0) {
      evens.push(nums[i]);
    }
  }
  return evens;
}
