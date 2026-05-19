import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Task {
  funcAdd(a: number, b: number, operation: 'add' | 'divide' = 'add'): number {
    if (operation === 'divide') {
      if (b === 0) {
        throw new Error('Cannot divide by zero');
      }
      return a / b;
    }

    return a + b;
  }

  funcValidateTitle(title: string): boolean {
    return title.length > 0;
  }
}
