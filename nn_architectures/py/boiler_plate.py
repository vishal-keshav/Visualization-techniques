# Contains tex header and footer boiler plate code

def header():
    header_tex_code = r"""
\documentclass{standalone}

\usepackage{tikz}
\usetikzlibrary{quotes}
\usepackage{tex/Box}

\definecolor{depthwisedark}{RGB}{94,238,118}
\definecolor{depthwise}{RGB}{131,249,151}
\definecolor{depthwiselight}{RGB}{171,255,185}

\definecolor{pointwisedark}{RGB}{255,193,98}
\definecolor{pointwise}{RGB}{252,210,147}
\definecolor{pointwiselight}{RGB}{253,226,184}

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
