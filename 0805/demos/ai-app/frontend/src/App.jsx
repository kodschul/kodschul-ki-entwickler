import { useState } from 'react';
import { useQuery, useMutation, gql } from '@apollo/client';

const GET_TODOS = gql`
  query GetTodos {
    todos {
      id
      title
      completed
      createdAt
    }
  }
`;

const CREATE_TODO = gql`
  mutation CreateTodo($title: String!) {
    createTodo(title: $title) {
      id
      title
      completed
      createdAt
    }
  }
`;

const TOGGLE_TODO = gql`
  mutation ToggleTodo($id: ID!) {
    toggleTodo(id: $id) {
      id
      completed
    }
  }
`;

const DELETE_TODO = gql`
  mutation DeleteTodo($id: ID!) {
    deleteTodo(id: $id)
  }
`;

export default function App() {
  const [inputValue, setInputValue] = useState('');

  const { data, loading, error } = useQuery(GET_TODOS);

  const [createTodo] = useMutation(CREATE_TODO, {
    refetchQueries: [{ query: GET_TODOS }],
  });

  const [toggleTodo] = useMutation(TOGGLE_TODO);

  const [deleteTodo] = useMutation(DELETE_TODO, {
    refetchQueries: [{ query: GET_TODOS }],
  });

  const handleAdd = async (e) => {
    e.preventDefault();
    const title = inputValue.trim();
    if (!title) return;
    await createTodo({ variables: { title } });
    setInputValue('');
  };

  const handleToggle = (id) => {
    toggleTodo({
      variables: { id },
      optimisticResponse: {
        toggleTodo: {
          __typename: 'Todo',
          id,
          completed: !data.todos.find(t => t.id === id)?.completed,
        },
      },
    });
  };

  const handleDelete = (id) => {
    deleteTodo({ variables: { id } });
  };

  const completedCount = data?.todos.filter(t => t.completed).length ?? 0;
  const totalCount = data?.todos.length ?? 0;

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.heading}>Todo List</h1>

        <form onSubmit={handleAdd} style={styles.form}>
          <input
            type="text"
            placeholder="What needs to be done?"
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}
            style={styles.input}
          />
          <button type="submit" style={styles.addButton}>Add</button>
        </form>

        {loading && <p style={styles.status}>Loading...</p>}
        {error && <p style={{ ...styles.status, color: '#e53e3e' }}>Error: {error.message}</p>}

        {data && (
          <>
            <p style={styles.counter}>{completedCount} / {totalCount} completed</p>
            <ul style={styles.list}>
              {data.todos.map(todo => (
                <li key={todo.id} style={styles.item}>
                  <button
                    onClick={() => handleToggle(todo.id)}
                    style={{
                      ...styles.checkbox,
                      background: todo.completed ? '#667eea' : 'transparent',
                      borderColor: todo.completed ? '#667eea' : '#cbd5e0',
                    }}
                    aria-label="Toggle todo"
                  >
                    {todo.completed && (
                      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
                        <path d="M2 6l3 3 5-5" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                      </svg>
                    )}
                  </button>
                  <span style={{
                    ...styles.title,
                    textDecoration: todo.completed ? 'line-through' : 'none',
                    color: todo.completed ? '#a0aec0' : '#2d3748',
                  }}>
                    {todo.title}
                  </span>
                  <button
                    onClick={() => handleDelete(todo.id)}
                    style={styles.deleteButton}
                    aria-label="Delete todo"
                  >
                    &times;
                  </button>
                </li>
              ))}
            </ul>
            {totalCount === 0 && (
              <p style={styles.empty}>No todos yet. Add one above!</p>
            )}
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: '100vh',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    display: 'flex',
    alignItems: 'flex-start',
    justifyContent: 'center',
    padding: '60px 16px',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  },
  card: {
    background: '#fff',
    borderRadius: '16px',
    boxShadow: '0 20px 60px rgba(0,0,0,0.2)',
    padding: '40px',
    width: '100%',
    maxWidth: '520px',
  },
  heading: {
    margin: '0 0 28px 0',
    fontSize: '28px',
    fontWeight: 700,
    color: '#2d3748',
    textAlign: 'center',
    letterSpacing: '-0.5px',
  },
  form: {
    display: 'flex',
    gap: '10px',
    marginBottom: '20px',
  },
  input: {
    flex: 1,
    padding: '12px 16px',
    fontSize: '15px',
    border: '2px solid #e2e8f0',
    borderRadius: '10px',
    outline: 'none',
    color: '#2d3748',
    transition: 'border-color 0.2s',
  },
  addButton: {
    padding: '12px 22px',
    fontSize: '15px',
    fontWeight: 600,
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: '#fff',
    border: 'none',
    borderRadius: '10px',
    cursor: 'pointer',
    whiteSpace: 'nowrap',
  },
  counter: {
    margin: '0 0 12px 0',
    fontSize: '13px',
    color: '#a0aec0',
    textAlign: 'right',
  },
  status: {
    textAlign: 'center',
    color: '#718096',
    fontSize: '14px',
  },
  list: {
    listStyle: 'none',
    margin: 0,
    padding: 0,
    display: 'flex',
    flexDirection: 'column',
    gap: '8px',
  },
  item: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    padding: '14px 16px',
    background: '#f7fafc',
    borderRadius: '10px',
    transition: 'background 0.15s',
  },
  checkbox: {
    width: '22px',
    height: '22px',
    borderRadius: '6px',
    border: '2px solid',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
    flexShrink: 0,
    transition: 'all 0.2s',
  },
  title: {
    flex: 1,
    fontSize: '15px',
    lineHeight: 1.4,
    transition: 'all 0.2s',
  },
  deleteButton: {
    background: 'none',
    border: 'none',
    color: '#cbd5e0',
    fontSize: '20px',
    lineHeight: 1,
    cursor: 'pointer',
    padding: '0 4px',
    flexShrink: 0,
    transition: 'color 0.15s',
  },
  empty: {
    textAlign: 'center',
    color: '#a0aec0',
    fontSize: '14px',
    marginTop: '20px',
  },
};
