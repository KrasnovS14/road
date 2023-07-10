from main import app

# Вход в аккаунт
@app.get('/login')
async def login_user_api(phone_number: int, password: str):
    result = login_user_api(phone_number=phone_number, password=password)

    return {'status': 1, 'message': result}


# вывод информации пользователя
@app.get('/user-cabinet')
async def get_user_cabinet(user_id: int):
    result = get_user_cabinet(user_id=user_id)

    return {'status': 1, 'message': result}