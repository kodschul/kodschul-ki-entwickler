// Beispiel-Test zur Orientierung.
// Dieser Test zeigt, wie die Teststruktur aussehen soll.
// Deine eigenen Tests kommen in separate Dateien.

import { TaskService } from '../src/TaskService';

describe('TaskService – Beispiel', () => {
  let service: TaskService;

  beforeEach(() => {
    service = new TaskService();
  });

  it('sollte eine neue Aufgabe erstellen', () => {
    const task = service.createTask({
      title: 'Login implementieren',
      description: 'OAuth2 Flow einrichten',
      priority: 'HIGH',
      projectId: 'PROJ-0001',
      tags: ['auth', 'backend'],
    });

    expect(task.id).toBeDefined();
    expect(task.title).toBe('Login implementieren');
    expect(task.status).toBe('OPEN');
    expect(task.tags).toContain('auth');
  });

  it('sollte einen Fehler werfen wenn der Titel leer ist', () => {
    expect(() =>
      service.createTask({
        title: '',
        description: 'Test',
        priority: 'LOW',
        projectId: 'PROJ-0001',
        tags: [],
      })
    ).toThrow('Aufgabentitel darf nicht leer sein');
  });
});
