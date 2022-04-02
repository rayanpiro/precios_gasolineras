# WhatsGas

WhatsGas es un proyecto para practicar la inyección de dependencias y evitar el acoplamiento entre las librerias utilizadas y la lógica del producto.

Sé que es mejorable tanto el código (asyncio entre otras) como el deploy (gunicorn por ejemplo), pero el fin era hacer un POC.

De todos modos con los precios de la gasolina puede incluso ser util para alguien. :smile:

Modo de uso.

Para construir la imagen.
```
docker build . -t gasolineras
```

Para arrancar el contenedor.
```
docker run --rm -it -p 5000:5000 --name gasolineras gasolineras
```