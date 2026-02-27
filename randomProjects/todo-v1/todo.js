const input = document.getElementById('todoInput');
const list = document.getElementById('todoList');

input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') addTodo();
});

function addTodo() {
  const text = input.value.trim();
  if (!text) return;

  const li = document.createElement('li');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';

  checkbox.addEventListener('change', () => {
    label.style.textDecoration = checkbox.checked ? 'line-through' : '';
  });

  const label = document.createElement('span');
  label.textContent = ' ' + text;

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete';
  deleteBtn.onclick = () => li.remove();

  li.appendChild(checkbox);
  li.appendChild(label);
  li.appendChild(deleteBtn);
  list.appendChild(li);

  input.value = '';
  input.focus();
}