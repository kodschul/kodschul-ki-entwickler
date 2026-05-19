import { ComponentFixture, TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App security and robustness', () => {
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

  it('keeps edited description payload as text and does not inject elements', () => {
    createTodo('Secure item');

    const item = compiled.querySelector('.todo-list li') as HTMLElement;
    item.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const editDescription = compiled.querySelector('.edit-description') as HTMLTextAreaElement;
    const payload = '<svg onload=alert(1)>payload';

    editDescription.value = payload;
    editDescription.dispatchEvent(new Event('input'));
    editDescription.dispatchEvent(new Event('blur'));
    fixture.detectChanges();

    const cancelButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    cancelButton.dispatchEvent(new MouseEvent('mousedown'));
    cancelButton.click();
    fixture.detectChanges();

    const description = compiled.querySelector('.todo-description');
    const injectedSvg = compiled.querySelector('.todo-description svg');

    expect(description?.textContent).toContain(payload);
    expect(injectedSvg).toBeNull();
  });

  it('allows saving edits on blur after a previous cancel action', () => {
    createTodo('Original title');

    const item = compiled.querySelector('.todo-list li') as HTMLElement;
    item.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const cancelButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    cancelButton.dispatchEvent(new MouseEvent('mousedown'));
    cancelButton.click();
    fixture.detectChanges();

    const reopen = compiled.querySelector('.todo-list li') as HTMLElement;
    reopen.dispatchEvent(new MouseEvent('dblclick'));
    fixture.detectChanges();

    const editTitle = compiled.querySelector('.edit-title') as HTMLInputElement;
    editTitle.value = 'Saved after cancel';
    editTitle.dispatchEvent(new Event('input'));
    editTitle.dispatchEvent(new Event('blur'));
    fixture.detectChanges();

    const closeEditButton = compiled.querySelector('.cancel-edit-btn') as HTMLButtonElement;
    closeEditButton.dispatchEvent(new MouseEvent('mousedown'));
    closeEditButton.click();
    fixture.detectChanges();

    expect(compiled.querySelector('.todo-title')?.textContent).toContain('Saved after cancel');
  });
});
