.PHONY: the_quadratic_formula.pdf all clean

the_quadratic_formula.pdf: the_quadratic_formula.tex
	latexmk -xelatex -view=none -use-make the_quadratic_formula.tex

clean:
	latexmk -CA
