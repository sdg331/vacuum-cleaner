import { useEffect, useState } from "react";
import TodoForm from "./components/TodoForm.jsx";
import TodoList from "./components/TodoList.jsx";
import { getTodos, createTodo, updateTodo, deleteTodo } from "./api/todoApi.js";

function App() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // 초기 로딩
  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    try {
      setLoading(true);
      setError("");
      const data = await getTodos();
      setTodos(data);
    } catch (err) {
      console.error(err);
      setError(err.message || "할 일 목록을 불러오는 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  const handleAdd = async (title) => {
    try {
      setError("");
      const newTodo = await createTodo(title);
      setTodos((prev) => [newTodo, ...prev]);
    } catch (err) {
      console.error(err);
      setError(err.message || "할 일을 추가하는 중 오류가 발생했습니다.");
    }
  };

  const handleToggle = async (id, completed) => {
    try:
      setError("");
      const updated = await updateTodo(id, { completed: !completed });
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)));
    } catch (err) {
      console.error(err);
      setError(err.message || "할 일 상태 변경 중 오류가 발생했습니다.");
    }
  };

  const handleDelete = async (id) => {
    try {
      setError("");
      await deleteTodo(id);
      setTodos((prev) => prev.filter((t) => t.id !== id));
    } catch (err) {
      console.error(err);
      setError(err.message || "할 일을 삭제하는 중 오류가 발생했습니다.");
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">📝 할 일 관리</h1>

      {error && <div className="error-box">{error}</div>}

      <TodoForm onAdd={handleAdd} />

      {loading ? (
        <p className="loading-text">로딩 중...</p>
      ) : (
        <>
          <TodoList
            todos={todos}
            onToggle={handleToggle}
            onDelete={handleDelete}
          />
          <div className="stats">
            <span>총 {todos.length}개</span>
            <span>
              완료 {todos.filter((t) => t.completed).length}개 / 미완료{" "}
              {todos.filter((t) => !t.completed).length}개
            </span>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
