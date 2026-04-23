from fastapi import FastAPI #import
from app.routes.issues import router as issues_router

app = FastAPI() 

app.include_router(issues_router)

#initializing fast api
#test 1

