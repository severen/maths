.PHONY: the_quadratic_formula.pdf all watch clean

all: the_quadratic_formula.pdf

the_quadratic_formula.pdf: the_quadratic_formula.tex
	latexmk -xelatex -use-make -f -quiet -interaction=nonstopmode $(PREVIEW_CONTINUOUSLY) the_quadratic_formula.tex

watch: PREVIEW_CONTINUOUSLY=-pvc -view=none
watch: the_quadratic_formula.pdf

clean:
	latexmk -CA
