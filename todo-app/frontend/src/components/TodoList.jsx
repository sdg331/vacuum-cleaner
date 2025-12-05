function TodoList({ todos, onToggle, onDelete }) {
  if (!todos.length) {
    return <p className="empty-text">등록된 할 일이 없습니다.</p>;
  }

  return (
    <ul className="todo-list">
      {todos.map((todo) => (
        <li
          key={todo.id}
          className={`todo-item ${todo.completed ? "completed" : ""}`}
        >
          <label className="todo-label">
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => onToggle(todo.id, todo.completed)}
            />
            <span>{todo.title}</span>
          </label>
          <button
            className="todo-delete-btn"
            onClick={() => onDelete(todo.id)}
          >
            삭제
          </button>
        </li>
      ))}
    </ul>
  );
}

export default TodoList;
