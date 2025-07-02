# FrameDirect

**FrameDirect** es una librería en Python para dibujar píxeles directamente en el framebuffer de Linux usando `mmap` y `pygame` para detectar la resolución de pantalla. Perfecta para proyectos que necesitan control directo del hardware gráfico sin depender de entornos gráficos como X11 o Wayland.


## Características

- Acceso directo al framebuffer `/dev/fb0`
- Dibujo de píxeles a bajo nivel
- Compatible con pantallas de 32 bits de color
- Colores predefinidos para facilitar el uso
- Colores en formato ARGB (en hexadecimal)
- Simple, ligera y sin dependencias pesadas (solo `pygame`)


## Requisitos

- Linux con framebuffer habilitado y acceso a `/dev/fb0`
- Python 3.6 o superior
- Paquete `pygame`


## Instalación

Puedes instalar la librería localmente:

```bash
pip install .

```

O directamente desde GitHub:

```bash
pip install git+https://github.com/tuusuario/FrameDirect.git

```

## Uso básico

```python
import FrameDirect

FrameDirect.init_FD()
FrameDirect.draw_pixel(100, 100, FrameDirect.RED)
FrameDirect.close()

```

## Licencia

MIT License


## Autor

Hecho con amor por gneval9 Software <3
Contacto: gneval99@gmail.com
