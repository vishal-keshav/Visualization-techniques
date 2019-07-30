# Contains tex header and footer boiler plate code

def header():
    header_tex_code = r"""
\documentclass[border=8pt, multi, tikz]{standalone}

\usepackage{import}
\subimport{./tex/}{init}

\usepackage{tikz}
\usetikzlibrary{quotes,arrows.meta}
\usetikzlibrary{positioning}
\usetikzlibrary{3d}
\usetikzlibrary{shapes.misc}

%Define the colors for different blocks
\definecolor{genericconvdark}{RGB}{255,193,98}
\definecolor{genericconv}{RGB}{252,210,147}
\definecolor{genericconvlight}{RGB}{253,226,184}

\definecolor{depthwisedark}{RGB}{94,238,118}
\definecolor{depthwise}{RGB}{131,249,151}
\definecolor{depthwiselight}{RGB}{171,255,185}

\definecolor{pointwisedark}{RGB}{255,193,98}
\definecolor{pointwise}{RGB}{252,210,147}
\definecolor{pointwiselight}{RGB}{253,226,184}

\definecolor{upconvdark}{RGB}{211, 104, 250}
\definecolor{upconv}{RGB}{215, 131, 246}
\definecolor{upconvlight}{RGB}{227, 163, 250}


% Connection style and colors for different operations
\definecolor{genericconvopcolor}{RGB}{253,226,184}
\newcommand{\genericconvop}{\tikz \draw[-Stealth,line width =1mm,draw=genericconvopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{pointwiseopcolor}{RGB}{11, 191, 131}
\newcommand{\pointwiseop}{\tikz \draw[-Stealth,line width =1mm,draw=pointwiseopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{depthwiseopcolor}{RGB}{94, 134, 247}
\newcommand{\depthwiseop}{\tikz \draw[-Stealth,line width =1mm,draw=depthwiseopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{upconvopcolor}{RGB}{247, 99, 99}
\newcommand{\upconvop}{\tikz \draw[-Stealth,line width =1mm,draw=upconvopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{depthwisepoolopcolor}{RGB}{94, 134, 247}
\newcommand{\depthwisepoolop}{\tikz \draw[-Stealth,line width =1mm,draw=depthwisepoolopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{pointwisepoolopcolor}{RGB}{94, 134, 247}
\newcommand{\pointwisepoolop}{\tikz \draw[-Stealth,line width =1mm,draw=pointwisepoolopcolor] (-0.3,0) -- ++(0.3,0);}

\definecolor{convpoolopcolor}{RGB}{94, 134, 247}
\newcommand{\convpoolop}{\tikz \draw[-Stealth,line width =1mm,draw=convpoolopcolor] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}

\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},opacity=0.7]

\tikzset{cross/.style={cross out, draw=black, minimum size=2*(#1-\pgflinewidth), inner sep=0pt, outer sep=0pt},
%default radius will be 1pt.
cross/.default={1pt}}
    """
    return header_tex_code

def footer():
    footer_tex_code = r"""
\end{tikzpicture}
\end{document}
    """
    return footer_tex_code
