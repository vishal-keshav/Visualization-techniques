import os
from py import boiler_plate as bp
from py import conv
from py import tex_code_constructor

def main():
    tex_code = bp.header() + "\n" + \
    conv.construct_conv_out([64,20,64], [0,0,0], [0,0,0], "depthwise",
        "depthwise conv", ["height", "width", "depth"], "depthwise") + "\n\n" + \
    conv.construct_conv_out([32,20,32], [0,0,0], [5,0,0], "depthwise",
        "pointwise conv", ["height", "width", "depth"], "pointwise") + "\n\n" + \
    bp.footer()
    print(tex_code)
    with open("sample.tex", "w") as f:
        f.write(tex_code)
    os.system("pdflatex sample")

if __name__ == "__main__":
    main()
