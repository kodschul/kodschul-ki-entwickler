import { useRef, useState } from 'react';

interface Props {
  onAdd: (title: string) => void;
}

export function TodoInput({ onAdd }: Props) {
  const [value, setValue] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const trimmed = value.trim();
    if (!trimmed) return;
    onAdd(trimmed);
    setValue('');
    inputRef.current?.focus();
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
      <input
        ref={inputRef}
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Add a new todo..."
        style={{ flex: 1, padding: '0.5rem' }}
        autoFocus
      />
      <button type="submit" style={{ padding: '0.5rem 1rem' }}>
        Add
      </button>
    </form>
  );
}
