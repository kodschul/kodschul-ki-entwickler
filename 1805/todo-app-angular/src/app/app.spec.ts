import { TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should create a todo and reset the input', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();

    const compiled = fixture.nativeElement as HTMLElement;
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = 'Buy milk';
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(1);
    expect(items[0].textContent).toContain('Buy milk');
    expect(items[0].textContent).toContain('Offen');
    expect(input.value).toBe('');
  });

  it('should reject empty todo input with a validation message', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();

    const compiled = fixture.nativeElement as HTMLElement;
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = '   ';
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
    fixture.detectChanges();

    expect(compiled.querySelectorAll('.todo-list li').length).toBe(0);
    expect(compiled.querySelector('.error')?.textContent).toContain('Bitte gib einen Titel ein.');
  });

  it('should create a todo when pressing Enter in the input', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();

    const compiled = fixture.nativeElement as HTMLElement;
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;

    input.value = 'Read a book';
    input.dispatchEvent(new Event('input'));
    input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(1);
    expect(items[0].textContent).toContain('Read a book');
  });
});
