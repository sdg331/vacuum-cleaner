// 백엔드 베이스 URL: http://localhost:5000/api 기준
const BASE_URL = "http://localhost:5000/api";

export async function getTodos() {
  const res = await fetch(`${BASE_URL}/todos`);
  if (!res.ok) {
    throw new Error("할 일 목록을 불러오지 못했습니다.");
  }
  return res.json();
}

export async function createTodo(title) {
  const res = await fetch(`${BASE_URL}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({}));
    throw new Error(error.error || "할 일을 추가하지 못했습니다.");
  }
  return res.json();
}

export async function updateTodo(id, payload) {
  const res = await fetch(`${BASE_URL}/todos/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({}));
    throw new Error(error.error || "할 일을 수정하지 못했습니다.");
  }
  return res.json();
}

export async function deleteTodo(id) {
  const res = await fetch(`${BASE_URL}/todos/${id}`, {
    method: "DELETE",
  });
  if (!res.ok && res.status !== 204) {
    throw new Error("할 일을 삭제하지 못했습니다.");
  }
}
