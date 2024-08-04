# CRUD de Películas con FastAPI

Este proyecto es una API CRUD para gestionar una base de datos de películas. La API está construida con FastAPI, utiliza autenticación JWT, se conecta a una base de datos SQLite mediante SQLAlchemy y genera documentación automática con Swagger.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- PyJWT

## Instalación en Local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

python -m venv venv
source venv/bin/activate  
# En Windows: venv\Scripts\activate


Link del swagger
[documentacion del api](https://movies-1-16a7.onrender.com/docs))


uvicorn main:app --reload
