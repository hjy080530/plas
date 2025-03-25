from typing import List

from fastAPI.applicationProgrammingDevelopment.ch05.model.todo import Todo, TodoResponse

_todos=[
    TodoResponse(
        todo_id=0,
        task="study fastapi",
        completed=0,
        created_at="2025-03-01"
    ),
    TodoResponse(
        todo_id=0,
        task="study db",
        completed=0,
        created_at="2025-03-01"
    ),
]
todo_id=1

def get_all() -> List[TodoResponse]:
    return _todos
def get_one(todo:Todo) ->TodoResponse:
    todo=next((x for x in _todos if x.task==_todos.task),None)
    return todo
