.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Runs main.py
	python3 main.py

format: ## Reformats all python files to the same formatting
	unify --in-place main.py
	unify --in-place cloaker.py