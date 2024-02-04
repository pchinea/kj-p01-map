import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from city_map_server.config import app_config


class SessionManager:
    session: AsyncSession
    async_session: async_sessionmaker

    def __init__(self):
        engine = create_async_engine(app_config.get_database_url)
        self.async_session = async_sessionmaker(engine, expire_on_commit=False)

    async def __aenter__(self):
        self.session = self.async_session()
        return self.session

    async def __aexit__(self, *_):
        await self.session.commit()
        await asyncio.shield(self.session.close())
