# Investment Report Generator | Upsonic

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Investment Report Generator example for [Upsonic](https://github.com/upsonic/upsonic) framework.

## Introduction

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

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Make (optional, for using Makefile commands)

### Clone the Repository

Using HTTPS:

```shell
git clone https://github.com/mertssmnoglu/upsonic-investment-report-generator.git
cd upsonic-investment-report-generator
```

Using SSH:

```shell
git clone git@github.com:mertssmnoglu/upsonic-investment-report-generator.git
cd upsonic-investment-report-generator
```

---

### Setup

Prepare the environment

```shell
uv venv --python 3.12
```

Activate the virtual environment.

```shell
source .venv/bin/activate
```

Install the dependencies

```shell
# Sync the dependencies according to the uv.lock file
uv sync
```

## Environment Variables

```shell
# Required
OPENAI_API_KEY=your_openai_api_key

# Optional, default is false
DEMO=true/false
```

You can copy `.env.example` as `.env` and fill in the required values.

```shell
cp .env.example .env
```

## Jupyter Notebook

This project includes a Jupyter Notebook for interactive exploration and analysis of investment data. You can find the notebook in the [notebooks](notebooks) directory.

## Demo App

Demo app introduces a command line investment report generator that generates detailed investment reports based on the provided company symbols(tickers).

Run the demo and see it in action:

```shell
make demo
```

## License

This project is licensed under the [MIT License](LICENSE).
