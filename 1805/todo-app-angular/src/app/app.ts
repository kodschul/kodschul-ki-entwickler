import { ChangeDetectionStrategy, Component, computed, signal } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';

interface TodoItem {
  id: number;
  title: string;
  description: string;
  dueDate: string | null;
  completed: boolean;
  createdAt: string;
  updatedAt: string | null;
}

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  protected readonly newTodoControl = new FormControl('', { nonNullable: true });
  protected readonly editTitleControl = new FormControl('', { nonNullable: true });
  protected readonly editDescriptionControl = new FormControl('', { nonNullable: true });
  protected readonly editDueDateControl = new FormControl<string | null>(null);
  protected readonly todos = signal<TodoItem[]>([]);
  protected readonly validationMessage = signal<string | null>(null);
  protected readonly editValidationMessage = signal<string | null>(null);
  protected readonly editingTodoId = signal<number | null>(null);
  protected readonly hasTodos = computed(() => this.todos().length > 0);

  private readonly nextId = signal(1);
  private suppressNextBlurSave = false;

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
        description: '',
        dueDate: null,
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: null,
      },
    ]);
    this.nextId.update((value) => value + 1);
    this.newTodoControl.setValue('');
    this.validationMessage.set(null);
  }

  protected onEnterCreate(event: Event): void {
    event.preventDefault();
    this.createTodo();
  }

  protected clearValidation(): void {
    if (this.validationMessage()) {
      this.validationMessage.set(null);
    }
  }

  protected startEditing(todo: TodoItem): void {
    this.editingTodoId.set(todo.id);
    this.editTitleControl.setValue(todo.title);
    this.editDescriptionControl.setValue(todo.description);
    this.editDueDateControl.setValue(todo.dueDate);
    this.editValidationMessage.set(null);
  }

  protected isEditing(todoId: number): boolean {
    return this.editingTodoId() === todoId;
  }

  protected clearEditValidation(): void {
    if (this.editValidationMessage()) {
      this.editValidationMessage.set(null);
    }
  }

  protected onCancelMouseDown(): void {
    this.suppressNextBlurSave = true;
  }

  protected cancelEdit(): void {
    this.editValidationMessage.set(null);
    this.editingTodoId.set(null);
  }

  protected saveEditOnBlur(): void {
    if (this.suppressNextBlurSave) {
      this.suppressNextBlurSave = false;
      return;
    }

    const todoId = this.editingTodoId();
    if (todoId === null) {
      return;
    }

    const title = this.editTitleControl.value.trim();
    if (!title) {
      this.editValidationMessage.set('Der Titel darf nicht leer sein.');
      return;
    }

    const description = this.editDescriptionControl.value.trim();
    const dueDate = this.editDueDateControl.value ? this.editDueDateControl.value : null;
    const updatedAt = new Date().toISOString();

    this.todos.update((existingTodos) =>
      existingTodos.map((todo) =>
        todo.id === todoId
          ? {
              ...todo,
              title,
              description,
              dueDate,
              updatedAt,
            }
          : todo,
      ),
    );
    this.editValidationMessage.set(null);
  }

  protected deleteTodo(todoId: number): void {
    const todoToDelete = this.todos().find((todo) => todo.id === todoId);
    if (!todoToDelete) {
      return;
    }

    const titleForPrompt = todoToDelete.title.trim();
    const confirmationMessage = titleForPrompt
      ? `Moechtest du "${titleForPrompt}" wirklich loeschen?`
      : 'Moechtest du dieses Todo wirklich loeschen?';

    const shouldDelete = window.confirm(confirmationMessage);
    if (!shouldDelete) {
      return;
    }

    this.todos.update((existingTodos) => existingTodos.filter((todo) => todo.id !== todoId));

    if (this.editingTodoId() === todoId) {
      this.cancelEdit();
    }
  }
}
