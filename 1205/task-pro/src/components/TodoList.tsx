import type { Todo } from '../types/todo';

interface Props {
  todos: Todo[];
}

export function TodoList({ todos }: Props) {
  if (todos.length === 0) {
    return <p style={{ color: '#888' }}>No todos yet. Add one above!</p>;
  }

  return (
    <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
      {todos.map((todo) => (
        <li
          key={todo.id}
          style={{
            padding: '0.5rem',
            borderBottom: '1px solid #eee',
            textDecoration: todo.completed ? 'line-through' : 'none',
            color: todo.completed ? '#aaa' : 'inherit',
          }}
        >
          {todo.title}
        </li>
      ))}
    </ul>
  );
}
