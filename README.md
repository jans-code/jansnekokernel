# jansnekokernel

![Logo](jansnekokernel/logo-svg.svg)

A very rough jupyter kernel implementation of [neko](https://www.nekovm.org).
There is no persistence whatsover, every cell is compiled and run without knowledge of previous cells.
Also there is no syntax highlighting.

## Dev Installation

- install neko from your package repository
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- then install kernelspec
- `jansnekokernel`
- or
- `jupyter kernelspec install --user jansnekokernel`

## Uninstall

- `jupyter kernelspec uninstall jansnekokernel`
- `pip uninstall jansnekokernel`
