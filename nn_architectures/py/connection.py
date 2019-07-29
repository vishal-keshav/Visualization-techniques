
def construct_connection_tex(node_name, out_pos, style):
    code ="\\draw [connection] ({}-east) -- node {{ \\{}}} ({},{},{});".format(
            node_name, style, out_pos[0], out_pos[1], out_pos[2]
    )
    return code

def construct_connection_pos_tex(in_pos, out_pos, style):
    code ="\\draw [connection] ({},{},{}) -- node {{ \\{}}} ({},{},{});".format(
      in_pos[0], in_pos[1], in_pos[2], style, out_pos[0], out_pos[1], out_pos[2]
    )
    return code

def add_connection_simple(node_name, in_pos, out_pos, type = "genericconvop"):
    if node_name == None:
        tex_code = construct_connection_pos_tex(in_pos, out_pos, type)
    else:
        tex_code = construct_connection_tex(node_name, out_pos, type)
    return tex_code

#[TODO]: Add the code for these connections
def add_connection_residual(in_pos, out_pos):
    pass

def add_connection_multiscale(in_pos, out_pos, inter_pos,
                    type1 = "genericconvop", type2 = "genericconvop"):
    pass
