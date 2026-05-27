export class SampleTodo {
    public Title: string;
    public IsDone: boolean;

    public constructor(Title: string, IsDone: boolean = false) {
        this.Title = Title;
        this.IsDone = IsDone;
    }

    public ToggleDone(): void {
        this.IsDone = !this.IsDone;
    }
}

export function CreateSampleTodo(): SampleTodo {
    return new SampleTodo("LearnTypeScript");
}
