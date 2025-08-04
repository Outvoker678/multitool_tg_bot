from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

# Создание асинхронного движка для SQLite
engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")

# Создание фабрики асинхронных сессий
async_session = async_sessionmaker(engine)

# Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Модель для таблицы users
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)

# Модель для таблицы friends (промежуточная таблица)
class Friend(Base):
    __tablename__ = "friends"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    friend_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

# Асинхронная функция для создания таблиц
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)