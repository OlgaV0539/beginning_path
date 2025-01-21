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


# Создание маршрута c параметром
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": f"Вы вошли как пользователь № {user_id}"}


# Создание маршрута c двумя параметрами
@app.get("/users/{user_name}/ages/{age_id}")
async def read_user_age(user_name: str, age_id: int):
    return {"user_name": user_name, "age_id": age_id, "name":
            f"Информация о пользователе. Имя:{user_name}, Возраст: {age_id}"}
