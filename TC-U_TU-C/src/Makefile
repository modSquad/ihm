all: TU-C.py TC-U.py
	@echo "Parsing du fichier XML..."
	@python TU-C.py > TU-C.tex
	@python TC-U.py > TC-U.tex
	pdflatex TC-U-full.tex
	@open TC-U-full.pdf

clean: 
	@rm -f TU-C.tex
	@rm -f TC-U.tex
