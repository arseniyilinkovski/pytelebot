from db import async_session
from db import Positions
from sqlalchemy import select, update


async def set_user(tg_id, first_name, index):
    async with async_session() as session:
        user = await session.scalar(select(Positions).where(Positions.tg_id == tg_id))

        if not user:
            session.add(Positions(tg_id=tg_id, first_name=first_name, id=index))
            await session.commit()


async def get_positions():
    async with async_session() as session:
        return await session.scalars(select(Positions))

