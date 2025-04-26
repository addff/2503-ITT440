# MUHAMMAD AMIRUL IMAN BIN MOHD ASHRAF
ITT440-Individual Assignment 

Student ID : 2023436086

# Introduction

Image processing is the field of computer science that focuses on performing operations on images to enhance them, extract useful information, or prepare them for further tasks such as recognition, analysis, or visualization, by applying techniques like filtering, resizing, color adjustment, and object detection.

# Tools

Pyvips is a fast and powerful Python library used for processing very large images quickly and efficiently, built on top of a C library called libvips.

# How It Works

Programs that use ``pyvips`` don't manipulate images directly, instead
they create pipelines of image processing operations building on a source
image. When the end of the pipe is connected to a destination, the whole
pipeline executes at once, streaming the image in parallel from source to
destination a section at a time.

Because ``pyvips`` is parallel, it's quick, and because it doesn't need to
keep entire images in memory, it's light.  For example, the libvips
speed and memory use benchmark:

https://github.com/libvips/libvips/wiki/Speed-and-memory-use

Loads a large tiff image, shrinks by 10%, sharpens, and saves again. On this
test ``pyvips`` is typically 3x faster than ImageMagick and needs 5x less
memory.

There's a handy chapter in the docs explaining how libvips opens files,
which gives some more background.

https://www.libvips.org/API/current/How-it-opens-files.html

# How to install Pyvips ?

Binary installation

The quickest way to start with pyvips is by installing the binary package
with:

    $ pip install "pyvips[binary]"

This installs a self-contained package with the most commonly needed
libraries. It should just work on most common platforms, including Linux,
Windows and macOS, with x64 and ARM CPUs.

If your platform is unsupported or the pre-built binary is
unsuitable, you can install libvips separately instead.

Local installation

You need the libvips shared library on your library search path, version 8.2
or later, though at least version 8.9 is required for all features to work.
See:

https://www.libvips.org/install.html

Linux
---------

Perhaps:

.. code-block:: shell

    $ sudo apt install libvips-dev --no-install-recommends
    $ pip install pyvips

With python 3.11 and later, you will need to create a venv first and add
`path/to/venv` to your `PATH`. Something like:

.. code-block:: shell

    $ python3 -m venv ~/.local
    $ pip install pyvips

macOS
--------

With Homebrew:

.. code-block:: shell

    $ brew install vips python pkg-config
    $ pip install pyvips

Windows
-----------

On Windows, you can download a pre-compiled binary from the libvips website.

https://www.libvips.org/install.html

You'll need a 64-bit Python. The official one works well.

You can add ``vips-dev-x.y\bin`` to your ``PATH``, but this will add a lot of
extra DLLs to your search path and they might conflict with other programs,
so it's usually safer to set ``PATH`` in your program.

To set ``PATH`` from within Python, you need something like this at the
start of your program:

    import os
    vipsbin = r'c:\vips-dev-8.16\bin'
    os.environ['PATH'] = vipsbin + ';' + os.environ['PATH']

For Python 3.8 and later, you need:


    import os
    vipsbin = r'c:\vips-dev-8.16\bin'
    add_dll_dir = getattr(os, 'add_dll_directory', None)
    if callable(add_dll_dir):
        add_dll_dir(vipsbin)
    else:
        os.environ['PATH'] = os.pathsep.join((vipsbin, os.environ['PATH']))

Now when you import pyvips, it should be able to find the DLLs.


# Code In Python
#!/usr/bin/python3

import sys
import pyvips

im = pyvips.Image.new_from_file(sys.argv[1], access="sequential")

text = pyvips.Image.text(f"<span color=\"red\">{sys.argv[3]}</span>",
                         width=500,
                         dpi=100,
                         align="centre",
                         rgba=True)

# scale the alpha down to make the text semi-transparent
text = (text * [1, 1, 1, 0.3]).cast("uchar")

text = text.rotate(45)

# tile to the size of the image page, then tile again to the full image size
text = text.embed(10, 10, text.width + 20, text.width + 20)
page_height = im.get_page_height()
text = text.replicate(1 + im.width / text.width, 1 + page_height / text.height)
text = text.crop(0, 0, im.width, page_height)
text = text.replicate(1, 1 + im.height / text.height)
text = text.crop(0, 0, im.width, im.height)

# composite the two layers
im = im.composite(text, "over")

im.write_to_file(sys.argv[2])
