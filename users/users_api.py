from main import app

# Вход в аккаунт
@app.get('/login')
async def login_user_api(phone_number: int, password: str):
    pass

# вывод информации пользователя
@app.get('/user-cabinet')
async def get_user_cabinet(user_id: int):
    pass