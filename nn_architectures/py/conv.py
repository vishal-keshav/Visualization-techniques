import os
import sys

def construct_conv_out(dims, origin, relative_pos, name = 'Convolution',
                        caption = "Convolution output", label = ['x','y','z'],
                        type = 'conv'):
    if type == 'depthwise':
        color = "depthwise"
    elif type == "pointwise":
        color = "pointwise"
    else:
        color = "generic_conv"
    absolute_pos = [origin[i]+relative_pos[i] for i in range(3)]
    from py.tex_code_constructor import construct_conv_tex
    return construct_conv_tex(absolute_pos, name, caption, label, color, dims)
