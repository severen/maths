.PHONY: how_to_prove_it.pdf all watch clean

all: how_to_prove_it.pdf

how_to_prove_it.pdf: how_to_prove_it.tex
	latexmk -lualatex -use-make -f -quiet -interaction=nonstopmode $(PREVIEW_CONTINUOUSLY) how_to_prove_it.tex

watch: PREVIEW_CONTINUOUSLY=-pvc -view=none
watch: how_to_prove_it.pdf

clean:
	latexmk -CA
