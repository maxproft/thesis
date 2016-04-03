import numpy as np
import pyopencl as cl

devices = [ d for d in cl.get_platforms()[0].get_devices(cl.device_type.GPU)]
