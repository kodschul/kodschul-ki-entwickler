import { Task } from './task';
import { Todo } from './todo';

describe('Service validation hardening', () => {
  it('rejects whitespace-only titles in the primary todo validator', () => {
    const service = new Todo();

    expect(service.funcValidateTodo('   ')).toBe(false);
  });

  it('rejects whitespace-only titles in secondary todo validator', () => {
    const service = new Todo();

    expect(service.funcValidateTodo2('   ')).toBe(false);
  });

  it('rejects whitespace-only titles in task title validation', () => {
    const service = new Task();

    expect(service.funcValidateTitle('   ')).toBe(false);
  });
});
