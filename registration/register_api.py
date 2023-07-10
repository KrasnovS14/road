from main import app
from datetime import datetime




# Регистрация пользователя
@app.post('/register-user')
async  def register_user_api(name: str, phone_number: int, password: str, ):
    result = register_user_api(phone_number=phone_number, name=name, password=password, reg_date=datetime.now())

    return {'status': 1, 'message': result}


# Регистрация автомобиля
@app.post('/register-user-cars')
async  def register_user_cars_api(name: str, car_model: str, car_number: int, tech_pass: str):
    result = register_user_cars_api(name=name, car_model=car_model, car_number=car_number, tech_pass=tech_pass)
    return {'status': 1, 'message': result}


# Регистрация штрафа
@app.post('/register-fine')
async def register_fine(tech_pass: str, car_number: int):
    result = register_fine(tech_pass=tech_pass, car_number=car_number)
    return {'status': 1, 'message': result}