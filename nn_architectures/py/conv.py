import os
import sys

def construct_conv_tex(pos, name, caption, label, color, dims):
    tex_code = "\\pic[shift={{({},{},{})}}] at (0,0,0)".format(pos[0], pos[1], pos[2]) + \
        "\n\t{{ Box={{ name={},caption= {},xlabel={{ {{ \"{}\", }} }}, ylabel = {}, zlabel = {},".format(name, caption, label[0], label[1], label[2]) + \
        "\n\tfillface={},".format(color+"dark") + \
        "\n\tfillfront={},".format(color+'light') + \
        "\n\tfill={}, height={},width={},depth={} }} }};".format(color, dims[0], dims[1], dims[2])
    return tex_code

def construct_depthconv_tex(pos, name, caption, label, color, dims):
    tex_code = "\\pic[shift={{({},{},{})}}] at (0,0,0)".format(pos[0], pos[1], pos[2]) + \
        "\n\t{{ RightBandedBox={{ name={},caption= {},xlabel={{ {{ \"{}\", }} }}, ylabel = {}, zlabel = {},".format(name, caption, label[0], label[1], label[2]) + \
        "\n\tfillface={},".format(color+"dark") + \
        "\n\tfillfront={},".format(color+'light') + \
        "\n\tbandfill={},".format(color) + \
        "\n\tfill={}, height={},width={},depth={} }} }};".format(color, dims[0], dims[1], dims[2])
    return tex_code

def construct_conv_out(dims, pos, name = 'Convolution',
          caption = "Convolution output", label = ['','',''], type = 'conv'):
    if type == 'depthwise':
        color = "depthwise"
        return construct_depthconv_tex(pos, name, caption, label, color, dims)
    elif type == "pointwise":
        color = "pointwise"
    else:
        color = "genericconv"
    return construct_conv_tex(pos, name, caption, label, color, dims)

#[TODO] Add the tex code for expansion
def construct_upconv_out(dims, pos, name = 'UpConvolution',
                        caption = "UpConvolution output", label = ['','',''],
                        type = 'upconv', input_coord = None):
    color = "upconv"
    return construct_conv_tex(pos, name, caption, label, color, dims)
