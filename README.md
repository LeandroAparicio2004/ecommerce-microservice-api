# E-Commerce API & Notification Microservice

Backend de una tienda online construido con arquitectura de microservicios. El sistema gestiona productos, órdenes de compra y notificaciones automáticas en tiempo real.

## ¿Qué hace este proyecto?

Cuando un cliente realiza una compra, el sistema:
1. Registra la orden y actualiza el stock de productos
2. Notifica automáticamente al servicio de notificaciones vía Redis
3. El servicio de notificaciones procesa el evento y simula el envío de un email al cliente

Todo esto ocurre de forma asíncrona, sin que un servicio dependa del otro para funcionar.

## Arquitectura

[ Cliente ] → [ Store Service :8000 ] → [ PostgreSQL ]

↓

[ Redis ]

↓

[ Notification Service ]

## Tecnologías

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Requisitos

- Docker Desktop instalado y corriendo

## Cómo ejecutar

1. Clonar el repositorio
bash
git clone https://github.com/tu-usuario/ecommerce-microservice-api.git
cd ecommerce-microservice-api

2. Levantar todos los servicios
bash
docker-compose up --build


3. Abrir la documentación interactiva
http://localhost:8000/docs

## Endpoints principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /products/ | Listar productos |
| POST | /products/ | Crear producto |
| PUT | /products/{id} | Actualizar producto |
| DELETE | /products/{id} | Eliminar producto |
| GET | /orders/ | Listar órdenes |
| POST | /orders/ | Crear orden de compra |

## Autor

**Leandro Aparicio** — [GitHub](https://github.com/LeandroAparicio2004)
