import { TestBed } from '@angular/core/testing';

import { Todo } from './todo';

describe('Todo', () => {
  let service: Todo;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Todo);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should validate todo title correctly', () => {
    expect(service.funcValidateTodo('')).toBeFalsy();
    expect(service.funcValidateTodo('   ')).toBeFalsy();
    expect(service.funcValidateTodo('Buy milk')).toBeTruthy();
  });

  it('should validate todo title correctly with funcValidateTodo2', () => {
    expect(service.funcValidateTodo2('')).toBeFalsy();
    expect(service.funcValidateTodo2('   ')).toBeFalsy();
    expect(service.funcValidateTodo2('Buy milk')).toBeTruthy();
  });

  it('should add two numbers correctly', () => {
    expect(service.funcAdd(1, 2)).toEqual(3);
    expect(service.funcAdd(-1, 1)).toEqual(0);
    expect(service.funcAdd(0, 0)).toEqual(0);
  });

  it('should format due date correctly', () => {
    const today = Math.floor(Date.now() / 1000);
    const tomorrow = today + 24 * 60 * 60;
    const yesterday = today - 24 * 60 * 60;

    expect(service.funcFormatDueDate(0)).toEqual('Kein Datum');
    expect(service.funcFormatDueDate(yesterday)).toEqual('Überfällig');
    const formattedTomorrow = service.funcFormatDueDate(tomorrow);
    expect(formattedTomorrow).toMatch(/Fällig am \d{2}\.\d{2}\.\d{4}/);
  });
});
