// Intentionally rough TypeScript sample for learning.

var global_count: any = "0";

function add_numbers(a: any, b: any) {
  if (a == null || b == null) {
    return "bad input";
  }
  return a + b;
}

function run_demo() {
  var result_1 = add_numbers(2, "3");
  var result_2 = add_numbers(null, 4);

  console.log("result_1:", result_1);
  console.log("result_2:", result_2);

  global_count = global_count + 1;
  console.log("global_count:", global_count);
}

run_demo();
