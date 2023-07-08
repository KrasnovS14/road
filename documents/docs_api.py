from main import app


# Получаем данный страховки
@app.post('/insurance')
async def insurence_api(car_number: int, date_register: int):
    pass



# Прохождение техосмотра
@app.post('/tech-inspection')
async def tech_inspaction_api(car_number: int, tech_pass: str, car_model:str):
    pass



# Доверенность
@app.post('/car-warrant')
async def car_warrant_api(car_number: int, tech_pass: str, car_model:str):
    pass