# Investment Report Generator | Upsonic

This advanced example shows how to build a sophisticated investment analysis system that combines market research, financial analysis, and portfolio management. The workflow uses a three-stage approach:

- Comprehensive stock analysis and market research
- Investment potential evaluation and ranking
- Strategic portfolio allocation recommendations

Key capabilities:

- Real-time market data analysis
- Professional financial research
- Investment risk assessment
- Portfolio allocation strategy
- Detailed investment rationale

Example companies to analyze:

- “AAPL, MSFT, GOOGL” (Tech Giants)
- “NVDA, AMD, INTC” (Semiconductor Leaders)
- “TSLA, F, GM” (Automotive Innovation)
- “JPM, BAC, GS” (Banking Sector)
- “AMZN, WMT, TGT” (Retail Competition)
- “PFE, JNJ, MRNA” (Healthcare Focus)
- “XOM, CVX, BP” (Energy Sector)

## Installation

```shell
git clone git@github.com:mertssmnoglu/upsonic-investment-report-generator.git
```

```shell
git clone https://github.com/mertssmnoglu/upsonic-investment-report-generator.git
```

---

## Usage

```shell
uv venv --python 3.12
```

```shell
source .venv/bin/activate.fish
```

Start the server on port 8000

```shell
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Developer must-use commands

### Save uv dependencies to requirements.txt

```shell
# Sync requirements.txt with uv
uv pip freeze > requirements.txt
```

```shell
pip install -r requirements.txt
```

## Docker

```shell
docker build -t upsonic-investment-report-generator .
```

```shell
docker run -p 8000:8000 --env-file .env upsonic-investment-report-generator:latest
```
