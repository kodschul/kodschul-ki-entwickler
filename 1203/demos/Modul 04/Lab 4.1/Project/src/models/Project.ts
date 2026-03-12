export type ProjectStatus = 'PLANNING' | 'ACTIVE' | 'ON_HOLD' | 'COMPLETED' | 'ARCHIVED';

export interface Project {
  id: string;
  name: string;
  description: string;
  status: ProjectStatus;
  ownerId: string;
  memberIds: string[];
  startDate: Date;
  endDate?: Date;
  createdAt: Date;
}

export type CreateProjectInput = Omit<Project, 'id' | 'createdAt' | 'status'>;
