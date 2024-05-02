(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("neurips_2023" "preprint") ("inputenc" "utf8") ("fontenc" "T1") ("algpseudocode" "noend")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "neurips_2023"
    "inputenc"
    "fontenc"
    "hyperref"
    "url"
    "booktabs"
    "amsfonts"
    "nicefrac"
    "microtype"
    "xcolor"
    "amsmath"
    "amssymb"
    "listings"
    "graphicx"
    "algorithm"
    "algpseudocode")
   (LaTeX-add-labels
    "alg:A$^*$"
    "alg:RBFS"
    "table:resultsMan"
    "table:resultsOther"))
 :latex)

