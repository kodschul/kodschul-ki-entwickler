import { User, UserRole, CreateUserInput } from './models/User';

export class UserService {
  private users: Map<string, User> = new Map();
  private idCounter = 0;

  private generateId(): string {
    return `USR-${String(++this.idCounter).padStart(4, '0')}`;
  }

  createUser(input: CreateUserInput): User {
    if (!input.username || input.username.trim() === '') {
      throw new Error('Benutzername darf nicht leer sein');
    }
    if (input.username.length < 3) {
      throw new Error('Benutzername muss mindestens 3 Zeichen lang sein');
    }
    if (!input.email || !input.email.includes('@')) {
      throw new Error('Ungültige E-Mail-Adresse');
    }

    // Prüfe auf Duplikate
    const existingByUsername = Array.from(this.users.values()).find(
      (u) => u.username.toLowerCase() === input.username.toLowerCase()
    );
    if (existingByUsername) {
      throw new Error(`Benutzername "${input.username}" ist bereits vergeben`);
    }

    const existingByEmail = Array.from(this.users.values()).find(
      (u) => u.email.toLowerCase() === input.email.toLowerCase()
    );
    if (existingByEmail) {
      throw new Error(`E-Mail "${input.email}" ist bereits registriert`);
    }

    const user: User = {
      ...input,
      id: this.generateId(),
      username: input.username.trim(),
      email: input.email.toLowerCase().trim(),
      isActive: true,
      createdAt: new Date(),
    };

    this.users.set(user.id, user);
    return user;
  }

  getUserById(id: string): User {
    const user = this.users.get(id);
    if (!user) {
      throw new Error(`Benutzer ${id} nicht gefunden`);
    }
    return user;
  }

  deactivateUser(id: string): User {
    const user = this.getUserById(id);
    if (!user.isActive) {
      throw new Error(`Benutzer ${id} ist bereits deaktiviert`);
    }
    const updated = { ...user, isActive: false };
    this.users.set(id, updated);
    return updated;
  }

  changeRole(id: string, newRole: UserRole): User {
    const user = this.getUserById(id);
    const updated = { ...user, role: newRole };
    this.users.set(id, updated);
    return updated;
  }

  getActiveUsers(): User[] {
    return Array.from(this.users.values()).filter((u) => u.isActive);
  }

  getUsersByRole(role: UserRole): User[] {
    return Array.from(this.users.values()).filter((u) => u.role === role);
  }
}
