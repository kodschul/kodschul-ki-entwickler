import { useTodos } from './hooks/useTodos';
import { TodoInput } from './components/TodoInput';
import { TodoList } from './components/TodoList';

export default function App() {
  const { todos, addTodo } = useTodos();

  return (
    <div style={{ maxWidth: '600px', margin: '2rem auto', padding: '0 1rem', fontFamily: 'sans-serif' }}>
      <h1>Task Pro</h1>
      <TodoInput onAdd={addTodo} />
      <TodoList todos={todos} />
    </div>
  );
}
