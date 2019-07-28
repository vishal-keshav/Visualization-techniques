# Contains tex header and footer boiler plate code

def header():
    header_tex_code = r"""
    \documentclass{standalone}

    \usepackage{tikz}
    \usetikzlibrary{quotes}
    \usepackage{tex/Box}

    \def\depthwise{rgb:green,10;red,2.5;white,5}

    \def\pointwise{rgb:yellow,5;red,2.5;white,5}

    \begin{document}

    \begin{tikzpicture}
    """
    return header_tex_code

def footer():
    footer_tex_code = r"""
    \end{tikzpicture}

    \end{document}
    """
    return footer_tex_code
