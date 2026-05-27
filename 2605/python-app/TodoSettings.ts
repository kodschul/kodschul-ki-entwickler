export class TodoSettings {
    public static readonly MaxTodos: number = 100;
    public static readonly DefaultPriority: number = 1;

    public AppName: string;
    public CurrentTodoCount: number;

    public constructor(AppName: string, CurrentTodoCount: number = 0) {
        this.AppName = AppName;
        this.CurrentTodoCount = CurrentTodoCount;
    }

    public CanAddMoreTodos(): boolean {
        const RemainingSlots: number = TodoSettings.MaxTodos - this.CurrentTodoCount;
        const HasCapacity: boolean = RemainingSlots > 0;
        return HasCapacity;
    }

    public BuildSummary(): string {
        const Summary: string = `${this.AppName}: ${this.CurrentTodoCount}/${TodoSettings.MaxTodos}`;
        return Summary;
    }
}
