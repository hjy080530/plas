from typing import List
from fastAPI.applicationProgrammingDevelopment.ch05.model.todo import TodoResponse, Todo
from fastAPI.applicationProgrammingDevelopment.ch05.fake import todo as data

def get_all() -> List[TodoResponse]:
    return data.get_all()

def get_one(todo: Todo) -> TodoResponse:
    return data.get_one(todo)