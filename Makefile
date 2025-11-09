# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = .

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean-github github

# Clean GitHub Pages files (but keep source directory)
clean-github:
	@echo "Cleaning GitHub Pages files from docs root..."
	@rm -rf .doctrees .buildinfo *.html *.js _static _sources _modules genindex.html search.html searchindex.js objects.inv

# GitHub Pages target: build HTML directly to docs root
github: clean-github
	@echo "Building HTML for GitHub Pages..."
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@touch .nojekyll
	@echo "Done! HTML files are in docs/ root for GitHub Pages"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 