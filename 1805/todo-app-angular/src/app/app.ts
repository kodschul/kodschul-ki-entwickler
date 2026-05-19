import { ChangeDetectionStrategy, Component, computed, signal } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';

interface TodoItem {
  id: number;
  title: string;
  completed: boolean;
  createdAt: string;
}

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class App {
  protected readonly newTodoControl = new FormControl('', { nonNullable: true });
  protected readonly todos = signal<TodoItem[]>([]);
  protected readonly validationMessage = signal<string | null>(null);
  protected readonly hasTodos = computed(() => this.todos().length > 0);

  private readonly nextId = signal(1);

  protected createTodo(): void {
    const title = this.newTodoControl.value.trim();

    if (!title) {
      this.validationMessage.set('Bitte gib einen Titel ein.');
      return;
    }

    this.todos.update((existingTodos) => [
      ...existingTodos,
      {
        id: this.nextId(),
        title,
        completed: false,
        createdAt: new Date().toISOString(),
      },
    ]);
    this.nextId.update((value) => value + 1);
    this.newTodoControl.setValue('');
    this.validationMessage.set(null);
  }

  protected onEnterCreate(event: KeyboardEvent): void {
    event.preventDefault();
    this.createTodo();
  }

  protected clearValidation(): void {
    if (this.validationMessage()) {
      this.validationMessage.set(null);
    }
  }
}
