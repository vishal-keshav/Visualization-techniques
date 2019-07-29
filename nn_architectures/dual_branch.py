"""
Author: Vishal Keshav
vishal.keshav.1993@gmail.com
"""

import os, sys

from py import conv
from py import connection
from py import img
from py import utility as util
from py import boiler_plate as bp

class draw_NN(object):
    """
    This module provides a bunch of helper functions to construct the NN with
    finetune tweaks over the visual results.

    Right now colors, desing , opacity etc are hard coded, but will be made
    tunable in setting option in future.
    """
    def __init__(self, name = "arch", relative_distance=5):
        self.name = name
        self.rel_dist = relative_distance
        self.tex_code = bp.header()
        self.prev_pos = [0,0,0]
        self.prev_node = None
        self.current_pos = [0,0,0]
        self.node_pos_tracker = {}

    def add_input(self, name, input_image, shape):
        """
        Input image is added at the current position, this is the first
        """
        tex_code_node = img.add_input(input_image, self.current_pos, shape)
        self.update(name, tex_code_node)
        self.prev_node = None

    def add_intermediate_input(self, name, input_image, shape):
        """
        Input can be added in between.
        """
        tex_code_node = connection.add_connection_simple(
                self.prev_node, self.prev_pos, self.current_pos,"genericconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = img.add_input(input_image, self.current_pos, shape)
        self.update(name, tex_code_node)
        self.prev_node = None

    def add_generic_conv_tensor(self, name, shape = [32,3,32],
                                        annotation = ["", "", ""]):
        """
        generic conv
        """
        tex_code_node = connection.add_connection_simple(
                self.prev_node, self.prev_pos, self.current_pos,"genericconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, name, annotation, "conv")
        self.update(name, tex_code_node)

    def add_depthwise_tensor(self, name, shape = [32,3,32],
                                        annotation = ["", "", ""]):
        """
        depthwise conv
        """
        tex_code_node = connection.add_connection_simple(
                 self.prev_node, self.prev_pos, self.current_pos, "depthwiseop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, name, annotation, "depthwise")
        self.update(name, tex_code_node)

    def add_pointwise_tensor(self, name, shape = [32,3,32],
                                        annotation = ["", "", ""]):
        """
        pointwise conv
        """
        tex_code_node = connection.add_connection_simple(
                 self.prev_node, self.prev_pos, self.current_pos, "pointwiseop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, name, annotation, "pointwise")
        self.update(name, tex_code_node)

    def add_upconv_tensor(self, name, shape = [32,3,32],
                                        annotation = ["", "", ""]):
        """
        transpose conv
        """
        tex_code_node = connection.add_connection_simple(
                    self.prev_node, self.prev_pos, self.current_pos, "upconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        # Needs to add the exand concept here
        tex_code_node =conv.construct_upconv_out(shape,self.current_pos,
                            name, name, annotation, "upconv")
        self.update(name, tex_code_node)

    def add_residual_multi(self, shape, node1, node2, convtype,
                                        depth=15, extent=5, early=3):
        """
        This is an expensive operation
        """
        in_pos = self.node_pos_tracker[node1]
        out_pos = self.node_pos_tracker[node2]
        pos1 = [in_pos[0], in_pos[1], in_pos[2]+depth]
        pos2 = [pos1[0]+extent, pos1[1], pos1[2]]# Draw box here
        pos3 = [out_pos[0]-early, pos2[1], pos2[2]]
        pos4 = [pos3[0], out_pos[1], out_pos[2]]# Draw concat here
        tex_code_node = connection.add_connection_simple(
                    None, in_pos, pos1, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = connection.add_connection_simple(
                    None, pos1, pos2, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        ## Adding conv here now
        tex_code_node = conv.construct_conv_out(shape, pos2,
                    "residualdepth1", "residualdepth1", ["","",""], "depthwise")
        #self.update(name, tex_code_node)
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = connection.add_connection_simple(
                    "residualdepth1", pos2, pos3, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = connection.add_connection_simple(
                    None, pos3, pos4, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        ## Draw concat here


    def update(self, name, code):
        """
        This is a small utility function
        """
        self.node_pos_tracker[name] = self.current_pos
        self.prev_pos = self.current_pos
        self.prev_node = name
        self.current_pos = util.update_pos(self.current_pos, self.rel_dist)
        self.tex_code = self.tex_code + util.spacing() + code

    def draw(self):
        self.tex_code = self.tex_code + util.spacing() + bp.footer()
        with open(self.name + ".tex", "w") as f:
            f.write(self.tex_code)
        try:
            os.system("pdflatex " + self.name)
            os.system("rm *.aux *.log")
            print("Generated " + self.name + ".pdf")
        except:
            print("Please install pdflatex!")

def main():
    draw_obj = draw_NN("arch_advance", 3)
    draw_obj.add_input("input", "in.jpeg", [128, 128])
    draw_obj.add_generic_conv_tensor(name = "convolution1",shape =[15,3,15])
    draw_obj.add_pointwise_tensor(name = "pointwise1", shape = [15,3,15])
    draw_obj.add_pointwise_tensor(name = "pointwise2pool", shape = [12,3,12])
    draw_obj.add_depthwise_tensor(name = "depthwise1", shape = [10,3,10])
    draw_obj.add_depthwise_tensor(name = "depthwise1pool", shape = [10,6,10])
    draw_obj.add_pointwise_tensor(name = "pointwise3", shape = [8,6,8])
    draw_obj.add_pointwise_tensor(name = "pointwise4pool", shape = [8,8,8])
    draw_obj.add_upconv_tensor(name = "upconv1", shape = [8,10,8])
    draw_obj.add_generic_conv_tensor(name ="convolution2", shape = [12,6,12])
    draw_obj.add_upconv_tensor(name = "upconv2", shape = [15,6,15])
    draw_obj.add_generic_conv_tensor(name ="convolution3", shape = [18,3,18])
    draw_obj.add_upconv_tensor(name = "upconv3", shape = [20,3,20])
    draw_obj.add_intermediate_input("output", "out.jpeg", [128, 128])
    draw_obj.add_residual_multi([12,3,12],"convolution1", "upconv3", "depthwise")
    draw_obj.add_residual_multi([10,3,10],"pointwise2pool", "upconv2",
                        "depthwise", depth = 10)
    draw_obj.add_residual_multi([8,3,8],"pointwise3", "upconv1", "depthwise",
                        depth = 6, extent = 3, early = 1)
    draw_obj.draw()

if __name__ == "__main__":
    main()
