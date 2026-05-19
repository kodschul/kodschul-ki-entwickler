export function greet(name: string): string {
  const prefix = 'Hello, ';
  return `${prefix}${name}!`;
}

console.log(greet('World'));
