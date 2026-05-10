import redis
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

def main():
    redis_host = os.getenv("REDIS_HOST", "redis")
    print("Notification Service iniciando...", flush=True)

    while True:
        try:
            r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
            r.ping()
            print("Conectado a Redis, escuchando ordenes...", flush=True)
            pubsub = r.pubsub()
            pubsub.subscribe("new_order")
            for message in pubsub.listen():
                print(f"Mensaje recibido: {message}", flush=True)
                if message["type"] == "message":
                    data = json.loads(message["data"])
                    print("----------------------------------", flush=True)
                    print(f"Nueva orden recibida!", flush=True)
                    print(f"ID de orden:    #{data['order_id']}", flush=True)
                    print(f"Cliente:        {data['customer_name']}", flush=True)
                    print(f"Email:          {data['customer_email']}", flush=True)
                    print(f"Estado:         {data['status']}", flush=True)
                    print(f"Notificacion enviada a {data['customer_email']}", flush=True)
                    print("----------------------------------", flush=True)
        except Exception as e:
            print(f"Error: {e}. Reintentando en 3 segundos...", flush=True)
            time.sleep(3)

if __name__ == "__main__":
    main()