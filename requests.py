from db import async_session
from db import Positions
from sqlalchemy import select, update, delete


async def set_user(tg_id, first_name, index, username):
    async with async_session() as session:
        user = await session.scalar(select(Positions).where(Positions.tg_id == tg_id))
        if user:
            return True
        if not user:
            session.add(Positions(tg_id=tg_id, first_name=first_name, id=index, username=username))
            await session.commit()


async def check_unique_position(index):
    all_categories = await get_positions()
    for position in all_categories:
        if int(position.id) == int(index):
            return False
    return True


async def get_positions():
    async with async_session() as session:
        return await session.scalars(select(Positions))


async def clear_table():
    async with async_session() as session:
        await session.delete()
        await session.commit()


