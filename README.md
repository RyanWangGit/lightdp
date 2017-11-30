# LightDP

A Light-Weight imperative language for developing provably privacy-preserving algorithms.
More details can be found [here](http://www.cse.psu.edu/~dbz5017/pub/popl17.pdf).

This project presents a tool for transforming LightDP programs into Python programs along with differential-privacy proofs.

# Install

To install it, run

```bash
$ python setup.py install
```

or use 

```bash
$ python setup.py develop
```

for dependencies installation without installing the program into system.

# Usage

The original python program 
To transform LightDP-annotated program `source.py` to `output.py`, run

```bash
$ lightdp source.py -o output.py
```

If `-o` is not given the default output file name is `source_t.py`.

This program can also run as a module like

```bash
$ python -m lightdp source.ldp -o output.py
```

# Examples

Examples can be found at `./examples`, currently `sparse_vector.py` and `sparse_vector_t.py` is included.