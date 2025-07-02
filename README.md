# FrameDirect

**FrameDirect** es una librería en Python para dibujar píxeles directamente en el framebuffer de Linux usando `mmap`. Perfecta para proyectos que necesitan control directo del hardware gráfico sin depender de entornos gráficos como X11 o Wayland.


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


## Instalación

Puedes instalar la librería localmente:

```bash
pip install .

```

O directamente desde GitHub:

```bash
pip install git+https://github.com/gneval9/FrameDirect.git
```

## Uso básico

```python
import framedirect

framedirect.init()
framedirect.resolution()

framedirect.draw_pixel(100, 100, framedirect.RED)

framedirect.close()
```

## Licencia

MIT License


## Autor

Hecho con amor por gneval9 Software <3
Contacto: gneval99@gmail.com
