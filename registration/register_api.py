from main import app

# Регистрация пользователя
@app.post('/register-user')
async  def register_user_api(name: str, phone_number: int):
    pass

# Регистрация автомобиля
@app.post('/register-user-cars')
async  def register_user_cars_api(name: str, car_model: str, car_number: int, tech_pass: str):
    pass


# Регистрация штрафа
@app.post('/register-fine')
async def register_fine(tech_pass: str, car_number: int):
    pass