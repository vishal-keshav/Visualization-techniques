"""
Construct tex codes for different types of diagrams
"""

def construct_conv_tex(pos, name, caption, label, color, dims):
    tex_code = "\\pic[shift={{({},{},{})}}] at (0,0,0)".format(pos[0], pos[1], pos[2]) + \
        "\n\t{{ Box={{ name={},caption= {},xlabel={{ {{ \"{}\", }} }}, ylabel = {}, zlabel = {},".format(name, caption, label[0], label[1], label[2]) + \
        "\n\tfill_face=\\{},".format(color+"dark") + \
        "\n\tfill=\\{}, height={},width={},depth={} }} }};".format(color, dims[0], dims[1], dims[2])
    return tex_code


###########Test##############
def main():
    print(construct_conv_tex([0,0,0],"name","caption",["x","y","z"], "color", [10,20,30]))

if __name__ == "__main__":
    main()


"""
        #"\n\tfill_face=\\{},".format(color+'_dark') + \
        #"\n\tfill_front=\\{},".format(color+'_light') + \
"""
