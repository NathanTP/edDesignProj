BUILD_DIR=build
# LATEX_ARGS="--output-directory=${BUILD_DIR}"
LATEX_ARGS=--output-directory=${BUILD_DIR}
#TEXMFOUTPUT="${BUILD_DIR}"

all:
	mkdir -p build
	xelatex ${LATEX_ARGS} pfa-asplos.tex
	# TEXMFOUTPUT="${BUILD_DIR}:" bibtex ${BUILD_DIR}/pfa-asplos.aux
	# TEXMFOUTPUT="${BUILD_DIR}:" makeglossaries -d ${BUILD_DIR} pfa-asplos
	xelatex ${LATEX_ARGS} pfa-asplos.tex
	xelatex ${LATEX_ARGS} pfa-asplos.tex
	mv build/pfa-asplos.pdf .

# all:
# 	mkdir -p build
# 	htlatex pfa-asplos.tex ${LATEX_ARGS}
# 	# TEXMFOUTPUT="${BUILD_DIR}:" bibtex ${BUILD_DIR}/pfa-asplos.aux
# 	# TEXMFOUTPUT="${BUILD_DIR}:" makeglossaries -d ${BUILD_DIR} pfa-asplos
# 	htlatex pfa-asplos.tex ${LATEX_ARGS}
# 	htlatex pfa-asplos.tex ${LATEX_ARGS}

.PHONY: clean
clean:
	rm -rf build

.PHONY: cleanall
cleanall: clean
	rm -f pfa-asplos.pdf
