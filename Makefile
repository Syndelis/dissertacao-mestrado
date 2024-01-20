all:
	pdflatex ufsj-abntex2.tex
	bibtex ufsj-abntex2
	pdflatex ufsj-abntex2.tex
	pdflatex ufsj-abntex2.tex

clean:
	rm -f *.aux *.bbl *.blg *.brf *.idx *.lof *.log *.synctex.gz *.toc
