from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import func


DATABASE_URL = 'postgresql://bagyshan:1@localhost/ecouse'
# """postgresql://username:password@host/db_name""" # Пример
engine = create_engine(DATABASE_URL) # связь между кодом и БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Это транзакция 

Base = declarative_base()

class Customer_warm(Base):
    __tablename__ = "customer_warm"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rashod_na_kv_m = Column(Integer)


Base.metadata.create_all(bind=engine)

Customer_warmPydentic = sqlalchemy_to_pydantic(Customer_warm, exclude=["id"])

db_customer_warm = Customer_warmPydentic(rashod_na_kv_m=0)

def create_customer_warm(db_customer_warm:Customer_warmPydentic):
    db_customer_warm = Customer_warm(**db_customer_warm.dict())
    with SessionLocal() as db:
        db.add(db_customer_warm)
        db.commit()
        db.refresh(db_customer_warm)
    return db_customer_warm

def get_customer_warm():
    result = []
    with SessionLocal() as db:
        customer_warms = db.query(Customer_warm).order_by(Customer_warm.id).all()
        for customer_warm in customer_warms:
            result.append({'id':customer_warm.id, 'rashod_na_kv_m':customer_warm.rashod_na_kv_m})
    return result


from decimal import Decimal

def get_avg_rashod():
    with SessionLocal() as db:
        average_rashod = db.query(func.avg(Customer_warm.rashod_na_kv_m)).scalar()

    # Преобразуем Decimal в float и форматируем до 2 знаков после запятой
    formatted_average_rashod = float(average_rashod) if average_rashod is not None else None

    return formatted_average_rashod





class Customer_water(Base):
    __tablename__ = "customer_water"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rashod_na_cheloveka = Column(Integer)


Base.metadata.create_all(bind=engine)

Customer_water_Pydentic = sqlalchemy_to_pydantic(Customer_water, exclude=["id"])

db_customer_water = Customer_water_Pydentic(rashod_na_cheloveka=0)

def create_customer_water(db_customer_water:Customer_water_Pydentic):
    db_customer_water = Customer_water(**db_customer_water.dict())
    with SessionLocal() as db:
        db.add(db_customer_water)
        db.commit()
        db.refresh(db_customer_water)
    return db_customer_water

def get_customer_water():
    result = []
    with SessionLocal() as db:
        customer_waters = db.query(Customer_water).order_by(Customer_water.id).all()
        for customer_water in customer_waters:
            result.append({'id':customer_water.id, 'rashod_na_cheloveka':customer_water.rashod_na_cheloveka})
    return result


def get_avg_rashod_water():
    with SessionLocal() as db:
        average_rashod = db.query(func.avg(Customer_water.rashod_na_cheloveka)).scalar()

    return average_rashod











class Customer_svet(Base):
    __tablename__ = "customer_svet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rashod_na_cheloveka = Column(Integer)


Base.metadata.create_all(bind=engine)

Customer_svet_Pydentic = sqlalchemy_to_pydantic(Customer_svet, exclude=["id"])

db_customer_svet = Customer_svet_Pydentic(rashod_na_cheloveka=0)

def create_customer_svet(db_customer_svet:Customer_svet_Pydentic):
    db_customer_svet = Customer_svet(**db_customer_svet.dict())
    with SessionLocal() as db:
        db.add(db_customer_svet)
        db.commit()
        db.refresh(db_customer_svet)
    return db_customer_svet

def get_customer_svet():
    result = []
    with SessionLocal() as db:
        customer_svets = db.query(Customer_svet).order_by(Customer_svet.id).all()
        for customer_svet in customer_svets:
            result.append({'id':customer_svet.id, 'rashod_na_cheloveka':customer_svet.rashod_na_cheloveka})
    return result


def get_avg_rashod_svet():
    with SessionLocal() as db:
        # Используем функцию func.avg() для вычисления среднего значения
        average_rashod = db.query(func.avg(Customer_svet.rashod_na_cheloveka)).scalar()

    return average_rashod











class Customer_gas(Base):
    __tablename__ = "customer_gas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rashod_na_cheloveka = Column(Integer)


Base.metadata.create_all(bind=engine)

Customer_gas_Pydentic = sqlalchemy_to_pydantic(Customer_gas, exclude=["id"])

db_customer_gas = Customer_gas_Pydentic(rashod_na_cheloveka=0)

def create_customer_gas(db_customer_gas:Customer_gas_Pydentic):
    db_customer_gas = Customer_gas(**db_customer_gas.dict())
    with SessionLocal() as db:
        db.add(db_customer_gas)
        db.commit()
        db.refresh(db_customer_gas)
    return db_customer_gas

def get_customer_gas():
    result = []
    with SessionLocal() as db:
        customer_gass = db.query(Customer_gas).order_by(Customer_gas.id).all()
        for customer_gas in customer_gass:
            result.append({'id':customer_gas.id, 'rashod_na_cheloveka':customer_gas.rashod_na_cheloveka})
    return result


def get_avg_rashod_gas():
    with SessionLocal() as db:
        # Используем функцию func.avg() для вычисления среднего значения
        average_rashod = db.query(func.avg(Customer_gas.rashod_na_cheloveka)).scalar()

    return average_rashod



















