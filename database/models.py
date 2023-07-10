from database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement= True, primary_key= True)
    phone_number = Column(Integer, nullable= False)
    name = Column(String, nullable=False)

    reg_date = Column(DateTime)


# Таблица паролей
class Password(Base):
    __tablename__ = 'user_password'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)
    pincode = Column(Integer)

    user_fk = relationship(User)



# Таблица категорий сервисов
class ServiceCategory(Base):
    __tablename__ = 'service_categories'
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    categories_name = Column(String, nullable=False)

    added_date = Column(DateTime)

# Таблица сервисов
class Service(Base):
    __tablename__ = 'services'
    service_id = Column(Integer, autoincrement=True, primary_key=True)
    service_category = Column(Integer, ForeignKey('service_categories.category_id'), nullable=False)
    service_name = Column(String, nullable= False)
    service_balance = Column(Float)
    service_check = Column(Integer, nullable=False)

    reg_date = Column(DateTime)


    category_fk = relationship(ServiceCategory)