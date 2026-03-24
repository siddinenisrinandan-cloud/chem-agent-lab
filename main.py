from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Chem Agent Lab API",
    description="Multi-Agent Chemistry Swarm System",
    version="1.0"
)

app.include_router(router)
