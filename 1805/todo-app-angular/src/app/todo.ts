export interface Todo {
    id: number;
    title: string;
    description: string;
    dueDate: string | null; // ISO date string or null
    createdDate: string; // ISO date string
}
