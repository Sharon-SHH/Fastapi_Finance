from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()
ALPHA_VANTAGE_API_KEY = "R9QNUET1NS6I0GXL"
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"

class StockRequest(BaseModel):
    symbol: str

@app.post("/stock-data")
async def get_stock_data(request: StockRequest):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": request.symbol,
        "apikey": ALPHA_VANTAGE_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(ALPHA_VANTAGE_BASE_URL, params=params)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Alpha Vantage")
        
        data = response.json()
        print(data)  # Print the data for debugging
        
        # Check for the correct key in the response JSON
        if "Time Series (Daily)" not in data:
            raise HTTPException(status_code=404, detail="Invalid symbol or data not available")
        
        time_series = data["Time Series (Daily)"]
        return {"symbol": request.symbol, "data": time_series}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
