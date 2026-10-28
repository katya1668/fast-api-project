from fastapi import FastAPI

# Создаем экземпляр приложения
app = FastAPI()

# Определяем корневой маршрут
@app.get("/00")
def read_root():
    return {"message": "Hello World"}