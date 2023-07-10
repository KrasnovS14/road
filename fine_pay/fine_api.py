from main import app


# Оплата штрафов
@app.get('/fine_pay')
async def fine_pay_api(car_number: int, tech_pass: str, car_model:str):
    result = fine_pay_api(car_number=car_number, tech_pass=tech_pass, car_model=car_model)
    return {'status': 1, 'message': result}



