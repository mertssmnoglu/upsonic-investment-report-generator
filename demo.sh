#!/bin/bash
git clone https://github.com/mertssmnoglu/upsonic-investment-report-generator.git
cd upsonic-investment-report-generator
uv venv --python 3.12
source .venv/bin/activate
uv sync
cp .env.example .env
make demo
