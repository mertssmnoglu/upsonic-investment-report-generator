from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app import GenerateInvestmentReport


from datetime import datetime
import asyncio
import json

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/generate-report")
async def generate_report(tickers: str):
    async def investment_report_stream(tickers: str):
        reporter = GenerateInvestmentReport()

        task = asyncio.create_task(reporter.run(tickers))

        while not task.done():
            try:
                data = await asyncio.wait_for(reporter.queue.get(), timeout=1.0)
                yield f"data: {json.dumps(data)}\n\n"
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                error_data = {
                    "status": "error",
                    "error": str(e),
                    "timestamp": datetime.now().isoformat(),
                }
                yield f"data: {json.dumps(error_data)}\n\n"
                break

        try:
            await task
            reporter.status = "completed"
        except Exception as e:
            error_data = {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            }
            yield f"data: {json.dumps(error_data)}\n\n"
            return

        while not reporter.queue.empty():
            try:
                data = await asyncio.wait_for(reporter.queue.get(), timeout=0.1)
                yield f"data: {json.dumps(data)}\n\n"
            except asyncio.TimeoutError:
                break

    return StreamingResponse(
        investment_report_stream(tickers),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
        },
    )
