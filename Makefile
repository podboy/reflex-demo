MAKEFLAGS += --always-make

VERSION ?= $(shell python3 -c "from myapp import __version__; print(__version__)")

version:
	@echo ${VERSION}

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .states .web reflex.lock backend.zip frontend.zip

run-development:
	reflex run --log-level debug --env dev
run-production:
	reflex run --log-level debug --env prod
