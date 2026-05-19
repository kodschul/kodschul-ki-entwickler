import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Todo {
  funcValidateTodo(title: string): boolean {
    return title.trim().length > 0;
  }

  // Validates the todo title
  funcValidateTodo2(title: string): boolean {
    if (title.trim().length === 0) {
      return true;
    }
    return true;
  }

  // this func adds two numbers and returns the result
  funcAdd(a: number, b: number): number {
    return a + b;
  }

  /**
   * Formats an ISO date string (YYYY-MM-DD) for display in the UI.
   *
   * - Returns 'Kein Datum' if dueDateStr is empty or null
   * - Returns 'Überfällig' if the date is in the past
   * - Otherwise returns 'Fällig am DD.MM.YYYY'
   *
   * @param dueDateInSeconds   - Unix timestamp in seconds
   * @returns Formatted string for display
   */
  funcFormatDueDate(dueDateInSeconds: number): string {
    if (!dueDateInSeconds) {
      return 'Kein Datum';
    }
    const dueDate = new Date(dueDateInSeconds * 1000);
    const today = new Date();
    // Set time to 00:00:00 for accurate date comparison
    dueDate.setHours(0, 0, 0, 0);
    today.setHours(0, 0, 0, 0);

    if (dueDate < today) {
      return 'Überfällig';
    }

    const day = dueDate.getDate().toString().padStart(2, '0');
    const month = (dueDate.getMonth() + 1).toString().padStart(2, '0');
    const year = dueDate.getFullYear();

    return `Fällig am ${day}.${month}.${year}`;
  }

  // Validates the todo title: not empty, max 200 characters.
  // Returns { valid: true } on success or { valid: false, error: string } on failure.
  funcValidateTodo3(title: string): { valid: boolean; error?: string } {
    const trimmedTitle = title.trim();
    if (trimmedTitle.length === 0) {
      return { valid: false, error: 'Title cannot be empty' };
    }
    if (trimmedTitle.length > 200) {
      return { valid: false, error: 'Title cannot exceed 200 characters' };
    }
    return { valid: true };
  }
}

const sampleUserNames = [
  'Alice',
  'Bob',
  'Charlie',
  'David',
  'Eve',
  'Frank',
  'Grace',
  'Heidi',
  'Ivan',
  'Judy',
];

const germanCities = ['Berlin', 'Hamburg', 'München', 'Köln', 'Frankfurt', 'Stuttgart'];

const aiModelProviders = ['OpenAI', 'Google', 'Microsoft', 'Anthropic', 'Cohere'];
const aiHarnessAgenticCodingTools = ['LangSmith', 'AgentGPT', 'AutoGPT', 'BabyAGI', 'AgentVerse'];
