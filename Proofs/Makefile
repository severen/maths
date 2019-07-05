.PHONY: proofs.pdf all watch clean

all: proofs.pdf

proofs.pdf: proofs.tex
	latexmk -xelatex -use-make -f -quiet -interaction=nonstopmode $(PREVIEW_CONTINUOUSLY) proofs.tex

watch: PREVIEW_CONTINUOUSLY=-pvc -view=none
watch: proofs.pdf

clean:
	latexmk -CA
