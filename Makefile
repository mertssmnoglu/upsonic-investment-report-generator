default: check

.PHONY:
clean-cache:
	@find . -type d -name "__pycache__" ! -path "./env/*" -exec rm -rf {} +
	@rm -rf .ruff_cache .pytest_cache

.PHONY:
clean-reports:
	@rm -f reports/demo_*

.PHONY:
clean-uv-cache:
	@uv cache clean

.PHONY:
check:
	@uv tool run ruff check .

.PHONY:
build:
	@uv build

.PHONY:
test:
	@uv tool run pytest

.PHONY:
format:
	@uv tool run ruff format .

.PHONY:
fix: format
	@uv tool run ruff check --fix

.PHONY:
demo:
	@DEMO=true uv run src/demo.py

.PHONY:
demo-workflow:
	@DEMO=true uv run src/demo_workflow.py

.PHONY:
run:
	@uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir src

.PHONY:
container-build:
	@docker build -t upsonic-investment-report-generator .

.PHONY:
container-dev:
	@docker run \
		--rm \
		-p 8000:8000 \
		--env-file .env \
		upsonic-investment-report-generator:latest
