#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansnekokernel
IPKernelApp.launch_instance(kernel_class=jansnekokernel)
