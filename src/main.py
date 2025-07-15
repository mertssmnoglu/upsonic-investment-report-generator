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

        initial_data = {
            "message": "Investment report generation started",
            "tickers": tickers,
            "timestamp": datetime.timestamp(datetime.now()),
        }
        yield f"data: {json.dumps(initial_data)}\n\n"

        while True:
            data = await reporter.queue.get()
            if data is None:
                break

            json_bytes = json.dumps(data).encode("utf-8") + b"\n"
            yield json_bytes

        async def stream():
            while not task.done():
                try:
                    data = await asyncio.wait_for(reporter.queue.get(), timeout=1.0)
                    yield f"data: {json.dumps(data)}\n\n"

                except Exception as e:
                    error_data = {
                        "status": "error",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat(),
                    }
                    yield f"data: {json.dumps(error_data)}\n\n"
                    break

            while not reporter.queue.empty():
                try:
                    data = await asyncio.wait_for(reporter.queue.get(), timeout=0.1)
                    yield f"data: {json.dumps(data)}\n\n"
                except asyncio.TimeoutError:
                    break

            final_data = {
                "message": "Investment report generation completed",
                "final_status": reporter.status,
                "timestamp": datetime.now().isoformat(),
            }
            yield f"data: {json.dumps(final_data)}\n\n"

            async for chunk in stream():
                yield chunk

    return StreamingResponse(
        investment_report_stream(tickers),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "text/plain; charset=utf-8",
        },
    )
