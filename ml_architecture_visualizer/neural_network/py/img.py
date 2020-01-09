import os

def construct_input_tex(file_name, pos, shape):
    code = "\\node[canvas is zy plane at x=0] ({}) at ({},{},{})".format(file_name, pos[0], pos[1], pos[2]) + \
    "\n{{\\includegraphics[width={}pt, height={}pt]{{{}}}}};".format(str(shape[0]), str(shape[1]), file_name)
    return code

def add_input(file_name, pos, shape):
    tex_code = construct_input_tex(file_name, pos, shape)
    return tex_code
