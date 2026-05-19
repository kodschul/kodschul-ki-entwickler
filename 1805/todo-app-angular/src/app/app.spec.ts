import { TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App', () => {
  function setup(): { fixture: any; compiled: HTMLElement } {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    return { fixture, compiled: fixture.nativeElement as HTMLElement };
  }

  function createTodo(compiled: HTMLElement, title: string): void {
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = title;
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
  }

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
    const { fixture, compiled } = setup();
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;

    createTodo(compiled, 'Buy milk');
    fixture.detectChanges();

    const items = compiled.querySelectorAll('.todo-list li');
    expect(items.length).toBe(1);
    expect(items[0].textContent).toContain('Buy milk');
    expect(input.value).toBe('');
  });

  it('should reject empty todo input with a validation message', () => {
    const { fixture, compiled } = setup();
    const input = compiled.querySelector('#todoTitle') as HTMLInputElement;
    const form = compiled.querySelector('form') as HTMLFormElement;

    input.value = '   ';
    input.dispatchEvent(new Event('input'));
    form.dispatchEvent(new Event('submit'));
    fixture.detectChanges();

    expect(compiled.querySelectorAll('.todo-list li').length).toBe(0);
    expect(compiled.querySelector('.error')?.textContent).toContain('Bitte gib einen Titel ein.');
  });

});
