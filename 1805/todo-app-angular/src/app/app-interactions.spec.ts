import { ComponentFixture, TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App interactions', () => {
  let fixture: ComponentFixture<App>;
  let compiled: HTMLElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    }).compileComponents();

    fixture = TestBed.createComponent(App);
    compiled = fixture.nativeElement as HTMLElement;
    fixture.detectChanges();
  });

  function createTodoWithSubmit(title: string): void {
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = title;
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
    fixture.detectChanges();
  }

  it('creates a todo when pressing Enter in the input', () => {
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;

    input.value = 'Read a book';
    input.dispatchEvent(new Event('input'));
    input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(1);
    expect(items[0].textContent).toContain('Read a book');
  });

  it('discards unsaved edit changes on cancel', () => {
    createTodoWithSubmit('Keep me');

    const item = compiled.querySelector('.todo-list li') as HTMLElement;
    item.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const editTitle = compiled.querySelector('.edit-title') as HTMLInputElement;
    editTitle.value = 'Unsaved change';
    editTitle.dispatchEvent(new Event('input'));

    const cancelButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    cancelButton.dispatchEvent(new MouseEvent('mousedown'));
    cancelButton.click();
    fixture.detectChanges();

    expect(compiled.querySelector('.edit-title')).toBeFalsy();
    expect(compiled.querySelector('.todo-title')?.textContent).toContain('Keep me');
  });

  it('renders potentially unsafe title text as escaped content', () => {
    const payload = '<img src=x onerror=alert(1)>script';
    createTodoWithSubmit(payload);

    const title = compiled.querySelector('.todo-title');
    const injectedImage = compiled.querySelector('.todo-title img');

    expect(title?.textContent).toContain(payload);
    expect(injectedImage).toBeNull();
  });

  it('deletes only the selected todo after confirmation', () => {
    createTodoWithSubmit('Todo alpha');
    createTodoWithSubmit('Todo beta');

    spyOn(window, 'confirm').and.returnValue(true);

    const deleteButtons = compiled.querySelectorAll('.delete-btn');
    (deleteButtons[0] as HTMLButtonElement).click();
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(1);
    expect(items[0].textContent).toContain('Todo beta');
    expect(items[0].textContent).not.toContain('Todo alpha');
  });

  it('keeps the todo list unchanged when deletion is canceled', () => {
    createTodoWithSubmit('Todo keep');
    createTodoWithSubmit('Todo keep too');

    spyOn(window, 'confirm').and.returnValue(false);

    const deleteButtons = compiled.querySelectorAll('.delete-btn');
    (deleteButtons[0] as HTMLButtonElement).click();
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(2);
    expect(items[0].textContent).toContain('Todo keep');
    expect(items[1].textContent).toContain('Todo keep too');
  });

  it('uses a safe fallback confirmation text when todo title is empty', () => {
    const app = fixture.componentInstance as any;

    app.todos.set([
      {
        id: 99,
        title: '   ',
        description: '',
        dueDate: null,
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: null,
      },
    ]);
    fixture.detectChanges();

    const confirmSpy = spyOn(window, 'confirm').and.returnValue(true);

    app.deleteTodo(99);
    fixture.detectChanges();

    expect(confirmSpy).toHaveBeenCalledWith('Moechtest du dieses Todo wirklich loeschen?');
    expect(compiled.querySelectorAll('.todo-list li').length).toBe(0);
  });
});
