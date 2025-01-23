from fastapi import FastAPI
from typing import Dict

# Создаем экземпляр приложения FastAPI
app = FastAPI()

users: Dict[str, Dict[str, str]] = {}


# Определение базового маршрута
@app.get("/")
async def root():
    return "Главная страница"


# Создание маршрута к странице администратора
@app.get("/user/admin")
async def user_admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def read_user_age(user_name: str, age_id: int):
    return f"Информация о пользователе. Имя: {user_name}, Возраст: {age_id}"
    
