from typing import List, Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlmodel import Field, SQLModel, Session, create_engine, select

class ResultBase(SQLModel):
    competence: float
    network_ability: float
    promoted: bool

class Result(ResultBase, table=True):
    __tablename__ = "data"

    id: Optional[int] = Field(default=None, primary_key=True)

class ResultRead(ResultBase):
    id: int

DESCRIPTION = """
API for the Quick Algorithm's Streaming Pipeline challenge.
"""

app = FastAPI(
    title="QA Data Streaming Mock API",
    description=DESCRIPTION,
    version="0.0.2",
)

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Streaming API</h1>"

@app.get('/api/v1/data', response_model=List[ResultRead])
def read_data(page: int):
    engine = create_engine('sqlite:////data/main.db')
    with Session(engine) as session:
        results = session.exec(
            select(Result).limit(10).offset(10*page)
        ).all()
    return results
