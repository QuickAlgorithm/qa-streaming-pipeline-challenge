from fastapi import FastAPI
from sqlalchemy import select

from orm.db import DBSession
from orm.result import ResultOrm
from schema.result import ResultSchema

DESCRIPTION = """
API for the Quick Algorithm's Streaming Pipeline challenge.
"""

app = FastAPI(
    title="QA Data Streaming Mock API",
    description=DESCRIPTION,
    version="0.0.2",
)


@app.get("/api/v1/data")
async def read_data(page: int, session: DBSession) -> list[ResultSchema]:
    results = (
        await session.scalars(select(ResultOrm).limit(10).offset(10 * page))
    ).all()
    return results
