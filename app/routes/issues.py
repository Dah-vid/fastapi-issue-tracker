import uuid # whats this
from fastapi import APIRouter, HTTPException, status #whats this
from app.schema import IssueCreate, IssueOut, IssueUpdate
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags= ["issues"])

@router.get("/", response_model=list[IssueOut]) # what does this do?
async def get_issues():
    """Retrtieve all issues.""" #whats a doc string
    issues = load_data() # what does this do?
    return issues

#what does everything below do
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create a new issue."""
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description, 
        "priority": payload.priority,
        "status": IssueStatus.open,
    }

    issues.append(new_issue)
    save_data(issues)
    return new_issue
