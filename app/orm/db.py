from typing import AsyncIterator, Annotated

from fastapi import Depends
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def async_session() -> AsyncIterator[AsyncSession]:
    engine = create_async_engine(
        "sqlite+aiosqlite:////data/main.db",
    )
    sessionmaker = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
    )
    async with sessionmaker() as session:
        yield session


DBSession = Annotated[AsyncSession, Depends(async_session)]
