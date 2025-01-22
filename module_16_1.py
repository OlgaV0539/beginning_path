from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Главная страница"}


# Создание маршрута к странице администратора
@app.get("/user/admin")
async def user_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/users/{user_name}/ages/{age_id}")
async def read_user_age(user_name: str, age_id: int):
    return {
        "message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age_id}"
    }
