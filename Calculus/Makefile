.PHONY: calculus.pdf all watch clean

all: calculus.pdf

calculus.pdf: calculus.tex
	latexmk -lualatex -use-make -f -quiet -interaction=nonstopmode -shell-escape $(PREVIEW_CONTINUOUSLY) calculus.tex

watch: PREVIEW_CONTINUOUSLY=-pvc -view=none
watch: calculus.pdf

clean:
	latexmk -CA
