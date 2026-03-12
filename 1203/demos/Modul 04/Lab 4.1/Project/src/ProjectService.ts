import { Project, ProjectStatus, CreateProjectInput } from './models/Project';
import { TaskService } from './TaskService';

export interface ProjectStats {
  totalTasks: number;
  openTasks: number;
  inProgressTasks: number;
  doneTasks: number;
  completionRate: number;
}

export class ProjectService {
  private projects: Map<string, Project> = new Map();
  private idCounter = 0;

  constructor(private taskService: TaskService) {}

  private generateId(): string {
    return `PROJ-${String(++this.idCounter).padStart(4, '0')}`;
  }

  createProject(input: CreateProjectInput): Project {
    if (!input.name || input.name.trim() === '') {
      throw new Error('Projektname darf nicht leer sein');
    }
    if (input.endDate && input.endDate <= input.startDate) {
      throw new Error('Enddatum muss nach dem Startdatum liegen');
    }
    if (!input.ownerId) {
      throw new Error('Eigentümer-ID ist erforderlich');
    }

    const project: Project = {
      ...input,
      id: this.generateId(),
      status: 'PLANNING',
      name: input.name.trim(),
      memberIds: input.memberIds ?? [],
      createdAt: new Date(),
    };

    this.projects.set(project.id, project);
    return project;
  }

  getProjectById(id: string): Project {
    const project = this.projects.get(id);
    if (!project) {
      throw new Error(`Projekt ${id} nicht gefunden`);
    }
    return project;
  }

  updateProjectStatus(id: string, status: ProjectStatus): Project {
    const project = this.getProjectById(id);

    const allowedTransitions: Record<ProjectStatus, ProjectStatus[]> = {
      PLANNING: ['ACTIVE', 'ARCHIVED'],
      ACTIVE: ['ON_HOLD', 'COMPLETED', 'ARCHIVED'],
      ON_HOLD: ['ACTIVE', 'ARCHIVED'],
      COMPLETED: ['ARCHIVED'],
      ARCHIVED: [],
    };

    if (!allowedTransitions[project.status].includes(status)) {
      throw new Error(
        `Statuswechsel von ${project.status} nach ${status} ist nicht erlaubt`
      );
    }

    const updated = { ...project, status };
    this.projects.set(id, updated);
    return updated;
  }

  addMember(projectId: string, userId: string): Project {
    const project = this.getProjectById(projectId);
    if (project.memberIds.includes(userId)) {
      throw new Error(`Benutzer ${userId} ist bereits Mitglied des Projekts`);
    }
    const updated = { ...project, memberIds: [...project.memberIds, userId] };
    this.projects.set(projectId, updated);
    return updated;
  }

  removeMember(projectId: string, userId: string): Project {
    const project = this.getProjectById(projectId);
    if (!project.memberIds.includes(userId)) {
      throw new Error(`Benutzer ${userId} ist kein Mitglied des Projekts`);
    }
    if (project.ownerId === userId) {
      throw new Error('Der Eigentümer kann nicht als Mitglied entfernt werden');
    }
    const updated = {
      ...project,
      memberIds: project.memberIds.filter((id) => id !== userId),
    };
    this.projects.set(projectId, updated);
    return updated;
  }

  deleteProject(id: string): void {
    this.getProjectById(id); // wirft Fehler wenn nicht gefunden

    // Alle zugehörigen Tasks löschen
    const tasks = this.taskService.getTasksByProject(id);
    for (const task of tasks) {
      this.taskService.deleteTask(task.id);
    }

    this.projects.delete(id);
  }

  getProjectStats(projectId: string): ProjectStats {
    this.getProjectById(projectId); // Existenz prüfen
    const tasks = this.taskService.getTasksByProject(projectId);
    const counts = {
      totalTasks: tasks.length,
      openTasks: tasks.filter((t) => t.status === 'OPEN').length,
      inProgressTasks: tasks.filter(
        (t) => t.status === 'IN_PROGRESS' || t.status === 'REVIEW'
      ).length,
      doneTasks: tasks.filter((t) => t.status === 'DONE').length,
      completionRate:
        tasks.length === 0
          ? 0
          : Math.round(
              (tasks.filter((t) => t.status === 'DONE').length / tasks.length) * 100
            ),
    };
    return counts;
  }

  getAllProjects(): Project[] {
    return Array.from(this.projects.values());
  }
}
