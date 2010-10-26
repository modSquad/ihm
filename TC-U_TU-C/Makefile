all: 
	cd src && ./TU-C.py > TU-C.tex && ./TC-U.py > TC-U.tex && pdflatex TC-U-full.tex && mv TC-U-full.pdf ../ && cd ..

clean: 
	@rm -f TU-C.tex
	@rm -f TC-U.tex
