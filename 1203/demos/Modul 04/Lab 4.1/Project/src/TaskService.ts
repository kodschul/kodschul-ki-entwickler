import { Task, TaskStatus, TaskPriority, CreateTaskInput, UpdateTaskInput } from './models/Task';

export class TaskService {
  private tasks: Map<string, Task> = new Map();
  private idCounter = 0;

  private generateId(): string {
    return `TASK-${String(++this.idCounter).padStart(5, '0')}`;
  }

  createTask(input: CreateTaskInput): Task {
    if (!input.title || input.title.trim() === '') {
      throw new Error('Aufgabentitel darf nicht leer sein');
    }
    if (input.title.length > 200) {
      throw new Error('Aufgabentitel darf maximal 200 Zeichen lang sein');
    }
    if (!input.projectId) {
      throw new Error('Projekt-ID ist erforderlich');
    }
    if (input.dueDate && input.dueDate < new Date()) {
      throw new Error('Fälligkeitsdatum darf nicht in der Vergangenheit liegen');
    }

    const task: Task = {
      ...input,
      id: this.generateId(),
      status: 'OPEN',
      title: input.title.trim(),
      tags: input.tags ?? [],
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    this.tasks.set(task.id, task);
    return task;
  }

  getTaskById(id: string): Task {
    const task = this.tasks.get(id);
    if (!task) {
      throw new Error(`Aufgabe ${id} nicht gefunden`);
    }
    return task;
  }

  updateTask(id: string, updates: UpdateTaskInput): Task {
    const task = this.getTaskById(id);

    if (updates.title !== undefined) {
      if (updates.title.trim() === '') {
        throw new Error('Aufgabentitel darf nicht leer sein');
      }
      if (updates.title.length > 200) {
        throw new Error('Aufgabentitel darf maximal 200 Zeichen lang sein');
      }
    }

    if (updates.dueDate && updates.dueDate < new Date()) {
      throw new Error('Fälligkeitsdatum darf nicht in der Vergangenheit liegen');
    }

    const updatedTask: Task = {
      ...task,
      ...updates,
      id: task.id,
      projectId: task.projectId,
      createdAt: task.createdAt,
      updatedAt: new Date(),
    };

    this.tasks.set(id, updatedTask);
    return updatedTask;
  }

  deleteTask(id: string): void {
    if (!this.tasks.has(id)) {
      throw new Error(`Aufgabe ${id} nicht gefunden`);
    }
    this.tasks.delete(id);
  }

  transitionStatus(id: string, newStatus: TaskStatus): Task {
    const task = this.getTaskById(id);

    const allowedTransitions: Record<TaskStatus, TaskStatus[]> = {
      OPEN: ['IN_PROGRESS', 'CANCELLED'],
      IN_PROGRESS: ['REVIEW', 'OPEN', 'CANCELLED'],
      REVIEW: ['DONE', 'IN_PROGRESS'],
      DONE: [],
      CANCELLED: [],
    };

    if (!allowedTransitions[task.status].includes(newStatus)) {
      throw new Error(
        `Statuswechsel von ${task.status} nach ${newStatus} ist nicht erlaubt`
      );
    }

    return this.updateTask(id, { status: newStatus });
  }

  getTasksByProject(projectId: string): Task[] {
    return Array.from(this.tasks.values()).filter(
      (task) => task.projectId === projectId
    );
  }

  getTasksByAssignee(assigneeId: string): Task[] {
    return Array.from(this.tasks.values()).filter(
      (task) => task.assigneeId === assigneeId
    );
  }

  getOverdueTasks(): Task[] {
    const now = new Date();
    return Array.from(this.tasks.values()).filter(
      (task) =>
        task.dueDate &&
        task.dueDate < now &&
        task.status !== 'DONE' &&
        task.status !== 'CANCELLED'
    );
  }

  getTasksByPriority(priority: TaskPriority): Task[] {
    return Array.from(this.tasks.values()).filter(
      (task) => task.priority === priority
    );
  }

  getTaskCountByStatus(): Record<TaskStatus, number> {
    const counts: Record<TaskStatus, number> = {
      OPEN: 0,
      IN_PROGRESS: 0,
      REVIEW: 0,
      DONE: 0,
      CANCELLED: 0,
    };
    for (const task of this.tasks.values()) {
      counts[task.status]++;
    }
    return counts;
  }
}
