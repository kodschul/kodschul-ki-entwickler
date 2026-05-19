import { ComponentFixture, TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App editing', () => {
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

  function createTodo(title: string): void {
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = title;
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
    fixture.detectChanges();
  }

  it('enters edit mode only for the selected todo', () => {
    createTodo('Todo one');
    createTodo('Todo two');

    const items = compiled.querySelectorAll('.todo-list li');
    items[1].dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    expect(items[1].querySelector('.edit-title')).toBeTruthy();
    expect(items[0].querySelector('.edit-title')).toBeFalsy();
  });

  it('auto-saves valid edit values on blur', () => {
    createTodo('Initial title');

    const item = compiled.querySelector('.todo-list li') as HTMLElement;
    item.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const editTitle = compiled.querySelector('.edit-title') as HTMLInputElement;
    const editDescription = compiled.querySelector('.edit-description') as HTMLTextAreaElement;
    const editDate = compiled.querySelector('.edit-date') as HTMLInputElement;

    editTitle.value = 'Updated title';
    editTitle.dispatchEvent(new Event('input'));
    editDescription.value = 'Updated description';
    editDescription.dispatchEvent(new Event('input'));
    editDate.value = '2026-12-24';
    editDate.dispatchEvent(new Event('input'));

    editTitle.dispatchEvent(new Event('blur'));
    editDescription.dispatchEvent(new Event('blur'));
    editDate.dispatchEvent(new Event('blur'));
    fixture.detectChanges();

    const cancelButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    cancelButton.dispatchEvent(new MouseEvent('mousedown'));
    cancelButton.click();
    fixture.detectChanges();

    expect(compiled.querySelector('.todo-title')?.textContent).toContain('Updated title');
    expect(compiled.querySelector('.todo-description')?.textContent).toContain('Updated description');
    expect(compiled.querySelector('.todo-date')?.textContent).toContain('2026-12-24');
  });

  it('shows a validation error and keeps the previous title for empty edits', () => {
    createTodo('Persisted title');

    const item = compiled.querySelector('.todo-list li') as HTMLElement;
    item.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const editTitle = compiled.querySelector('.edit-title') as HTMLInputElement;
    editTitle.value = '   ';
    editTitle.dispatchEvent(new Event('input'));
    editTitle.dispatchEvent(new Event('blur'));
    fixture.detectChanges();

    expect(compiled.querySelector('.error')?.textContent).toContain('Der Titel darf nicht leer sein.');

    const cancelButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    cancelButton.dispatchEvent(new MouseEvent('mousedown'));
    cancelButton.click();
    fixture.detectChanges();

    expect(compiled.querySelector('.todo-title')?.textContent).toContain('Persisted title');
  });
});
