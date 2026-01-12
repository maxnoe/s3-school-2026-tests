TEXOPTIONS=--lualatex --halt-on-error --interaction=nonstopmode --shell-escape --output-directory=build

all: build/testing.pdf


build/testing.pdf: FORCE build/license.pdf | build
	max_print_line=1048576 \
	TEXINPUTS=beamertheme-vertex: \
	latexmk $(TEXOPTIONS) testing.tex


preview: FORCE | build
	max_print_line=1048576 \
	TEXINPUTS=beamertheme-vertex: \
	latexmk -pvc $(TEXOPTIONS) testing.tex


build/license.pdf: | build
	wget -O build/license.svg https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg
	inkscape build/license.svg -o $@

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:


.PHONY: all clean FORCE
