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

    def add_intermediate_input(self, name, input_image, shape, space = 0):
        """
        Input can be added in between.
        """
        self.current_pos[0] = self.current_pos[0] + space
        tex_code_node = connection.add_connection_simple(
                self.prev_node, self.prev_pos, self.current_pos,"genericconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = img.add_input(input_image, self.current_pos, shape)
        self.update(name, tex_code_node)
        self.prev_node = None

    def add_generic_conv_tensor(self, name, shape = [32,3,32], caption = "",
                                        annotation = ["", "", ""], space = 0):
        """
        generic conv
        """
        self.current_pos[0] = self.current_pos[0] + space
        tex_code_node = connection.add_connection_simple(
                self.prev_node, self.prev_pos, self.current_pos,"genericconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, caption, annotation, "conv")
        self.update(name, tex_code_node)

    def add_depthwise_tensor(self, name, shape = [32,3,32], caption = "",
                                        annotation = ["", "", ""], space = 0):
        """
        depthwise conv
        """
        self.current_pos[0] = self.current_pos[0] + space
        tex_code_node = connection.add_connection_simple(
                 self.prev_node, self.prev_pos, self.current_pos, "depthwiseop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, caption, annotation, "depthwise")
        self.update(name, tex_code_node)

    def add_pointwise_tensor(self, name, shape = [32,3,32], caption = "",
                                        annotation = ["", "", ""], space = 0):
        """
        pointwise conv
        """
        self.current_pos[0] = self.current_pos[0] + space
        tex_code_node = connection.add_connection_simple(
                 self.prev_node, self.prev_pos, self.current_pos, "pointwiseop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = conv.construct_conv_out(shape, self.current_pos,
                            name, caption, annotation, "pointwise")
        self.update(name, tex_code_node)

    def add_upconv_tensor(self, name, shape = [32,3,32], caption = "",
                                        annotation = ["", "", ""], space = 0):
        """
        transpose conv
        """
        self.current_pos[0] = self.current_pos[0] + space
        tex_code_node = connection.add_connection_simple(
                    self.prev_node, self.prev_pos, self.current_pos, "upconvop")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        # Needs to add the exand concept here
        tex_code_node =conv.construct_upconv_out(shape,self.current_pos,
                            name, caption, annotation, "upconv")
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
                    "residualdepth1", "", ["","",""], "depthwise")
        #self.update(name, tex_code_node)
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = connection.add_connection_simple(
                    "residualdepth1", pos2, pos3, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        tex_code_node = connection.add_connection_simple(
                    None, pos3, pos4, convtype+"op")
        self.tex_code = self.tex_code + util.spacing() + tex_code_node
        ## Draw concat here
        tex_code = connection.add_concat(pos4)
        self.tex_code = self.tex_code + util.spacing() + tex_code


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
    draw_obj = draw_NN("lowlightarch", 2)
    draw_obj.add_input("input", "in.jpeg", [180, 180])
    draw_obj.add_generic_conv_tensor(name = "gconv11",shape =[32,1,32])
    draw_obj.add_pointwise_tensor(name = "gpointconv12", shape = [16,1,16])

    draw_obj.add_pointwise_tensor(name = "gconv21", shape = [16,2,16])
    draw_obj.add_pointwise_tensor(name = "gpointconv22", shape = [8,2,8])

    draw_obj.add_pointwise_tensor(name = "gconv31", shape = [8,4,8])
    draw_obj.add_pointwise_tensor(name = "gpointconv32", shape = [4,6,4])

    draw_obj.add_pointwise_tensor(name = "gconv41", shape = [4,6,4], space = 0.3)
    draw_obj.add_pointwise_tensor(name = "gpointconv42", shape = [2,8,2], space = 0.5)

    # Two times
    draw_obj.add_pointwise_tensor(name = "gconv52", shape = [1,8,1], space = 0.3)

    # Two times
    draw_obj.add_upconv_tensor(name = "gconv62",shape =[2,8,2], space = 0.8)

    # Two times
    draw_obj.add_upconv_tensor(name = "gconv72",shape =[4,6,4], space = 1.2)

    # Two times
    draw_obj.add_upconv_tensor(name = "gconv82",shape =[8,4,8], space = 0.8)

    # Two times
    draw_obj.add_upconv_tensor(name = "gconv92",shape =[16,2,16], space = 0.8)

    # One time
    draw_obj.add_generic_conv_tensor(name = "gconv10",shape =[32,1,32], space = 0.5)
    draw_obj.add_intermediate_input("output", "out.jpeg", [180, 180], space = -0.5)
    ## Adding residual connection 4
    draw_obj.add_residual_multi([4,8,4],"gconv41", "gconv62", "depthwise", depth = 6, extent = 2, early = -2)

    ## Adding residual connection 3
    draw_obj.add_residual_multi([8,4,8],"gconv31", "gconv72", "depthwise", depth = 10, early = -1.5)

    ## Adding residual connection 2
    draw_obj.add_residual_multi([16,2,16],"gconv21", "gconv82", "depthwise", depth = 15, early = -1.3)

    ## Adding residual connection 1
    draw_obj.add_residual_multi([32,1,32],"gconv11", "gconv92", "depthwise", depth = 25, early = -1.0)

    """draw_obj.add_residual_multi([12,3,12],"convolution1", "upconv3", "depthwise")
    draw_obj.add_residual_multi([10,3,10],"pointwise2pool", "upconv2",
                        "depthwise", depth = 10)
    draw_obj.add_residual_multi([8,3,8],"pointwise3", "upconv1", "depthwise",
                        depth = 6, extent = 3, early = 1)"""
    draw_obj.draw()

if __name__ == "__main__":
    main()
