#
# Generates the part of the docs that are, well, generated
#

PYTHON=python3
OUTDIR=../docs/samples

default : all

all : webfinger-samples actor-samples

webfinger-samples :
	[[ -d "$(OUTDIR)/webfinger" ]] || mkdir -p "$(OUTDIR)/webfinger"
	$(PYTHON) generate-samples/generate-samples.py --type webfinger --account-file generate-samples/sample-accounts.json --out $(OUTDIR)/webfinger/index.md

actor-samples :
	[[ -d "$(OUTDIR)/actor" ]] || mkdir -p "$(OUTDIR)/actor"
	$(PYTHON) generate-samples/generate-samples.py --type actor --account-file generate-samples/sample-accounts.json --out $(OUTDIR)/actor/index.md

.PHONY:
	default all webfinger-samples actor-samples
