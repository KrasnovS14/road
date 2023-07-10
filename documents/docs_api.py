from main import app


# Получаем данный страховки
@app.post('/insurance')
async def insurence_api(car_number: int, date_register: int):
    result = insurence_api(car_number=car_number, date_register=date_register)
    return {'status': 1, 'message': result}



# Прохождение техосмотра
@app.post('/tech-inspection')
async def tech_inspaction_api(car_number: int, tech_pass: str, car_model:str):
    result = tech_inspaction_api(car_number=car_number, tech_pass=tech_pass, car_model=car_model)
    return {'status': 1, 'message': result}



# Доверенность
@app.post('/car-warrant')
async def car_warrant_api(car_number: int, tech_pass: str, car_model:str):
    result = car_warrant_api(car_number=car_number, tech_pass=tech_pass, car_model=car_model)
    return {'status': 1, 'message': result}