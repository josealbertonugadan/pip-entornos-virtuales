# Pip y entornos virtuales
Curso de pip y entornos virtuales

## Game Project
Para ejecutar el juego sigue las siguientes instrucciones en la terminal:
```sh
cd game
python3 main.py
```
Y listo, el juego habrá comenzado!

## App Project
```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## Web Server Project
```sh
git clone
cd web-server
docker-compose build
docker-compose up -d
docker-compose ps
docker-compose exec web-server bash
python main.py
```