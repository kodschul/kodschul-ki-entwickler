import { greet } from './sample';

describe('greet', () => {
  it('returns a greeting with the provided name', () => {
    expect(greet('World')).toBe('Hello, World!');
  });

  it('supports empty strings', () => {
    expect(greet('')).toBe('Hello, !');
  });

  it('preserves whitespace in the name', () => {
    expect(greet('  Alex  ')).toBe('Hello,   Alex  !');
  });
});
