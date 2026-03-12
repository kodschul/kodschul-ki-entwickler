export type UserRole = 'ADMIN' | 'MANAGER' | 'DEVELOPER' | 'VIEWER';

export interface User {
  id: string;
  username: string;
  email: string;
  role: UserRole;
  isActive: boolean;
  createdAt: Date;
}

export type CreateUserInput = Omit<User, 'id' | 'createdAt' | 'isActive'>;
