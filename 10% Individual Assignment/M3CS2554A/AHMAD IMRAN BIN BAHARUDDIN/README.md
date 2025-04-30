### NAME : AHMAD IMRAN BAHARUDDIN
### STUDENT NO. : 2023240168
### TITLE : BASIC APPLICATION OF CVG USING PYCAIRO
----
![pycairo](https://github.com/user-attachments/assets/ebdec452-6b28-441b-8849-5cd96667668a)

#### Objectives:
 * To understand PyCairo tools used for cvg in Python
 * To develop high-quality graphics using PyCairo

#### PyCairo
  ~ PyCairo stands as a crucial Python binding for the robust Cairo graphics library, effectively bringing its powerful 2D rendering capabilities into the Python ecosystem. It empowers developers to programmatically generate high-quality vector graphics that remain crisp and clear regardless of scaling. Through pycairo, Python applications gain the ability to draw a diverse array of shapes, intricate paths, and text with precise control over styling, transformations, and compositing. Furthermore, its versatility extends to supporting multiple output formats, including popular image and vector file types, as well as various display backends, making it an invaluable tool for creating visualizations, diagrams, and other graphical elements within Python projects.
  
  ~ It is designed to match the cairo C API as closely as possible, and to deviate only in cases which are clearly better implemented in a more 'Pythonic' way.

#### Advantages of Using PyCairo
  - ``Powerful and Versatile Rendering``: PyCairo provides a comprehensive set of drawing primitives. You can create lines, curves (Bezier and elliptical arcs), rectangles, text, and even work with image data. This makes it suitable for a wide range of applications, from simple drawings to complex visualizations.

  - ``High-Quality Output``: Cairo, the underlying C library, is known for producing crisp and professional-looking graphics. It supports antialiasing, alpha compositing, and various rendering backends, ensuring your visuals look polished across different platforms and output formats.

  - ``Scriptability and Automation``: Python's scripting capabilities make PyCairo excellent for automating graphics generation. Whether you need to create charts, diagrams, or visualizations from data, PyCairo allows you to write scripts to produce these outputs programmatically.

  - ``Open Source and Cross-Platform``: PyCairo is open-source, meaning it's free to use and modify. Furthermore, it's cross-platform, running smoothly on Windows, macOS, and Linux, making it a consistent choice regardless of your operating system.
---
#### How To Use PyCairo
  1) Install PyCairo library
  ```
    pip3 install pycairo
  ```
  2) Open Python
  ```
    python3
  ```
  4) Start coding using PyCairo
---
#### Example Code
``` py
import math
import cairo

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(0, 0)
# Arc(cx, cy, radius, start_angle, stop_angle)
ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
ctx.line_to(0.5, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
ctx.close_path()

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
```

---
#### Example Output Using Code Above

