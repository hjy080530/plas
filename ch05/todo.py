router = APIRouter(prefix="/todo")

@router.get('')
def get_all() -> List[TodoResponse]:
    return service.get_all()

@router.get('/{task}')
def get_one(task:str) -> TodoResponse:
    return service.get_one(Todo(task=task))

