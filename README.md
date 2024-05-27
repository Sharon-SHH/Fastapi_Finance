# Fastapi_Finance
Use Alpha Vantage API

Starting a FastAPI app with Uvicorn:
`
uvicorn main:app --reload`

## Real-Time Stock Price Fetching and Analysis
In this example, we'll create a FastAPI application that fetches real-time stock prices from a public API (e.g., Alpha Vantage) and calculates simple moving averages (SMA) asynchronously.

### Test
1. Access the interactive API documentation at http://127.0.0.1:8000/docs to test the endpoints.
`POST to /stock-data with JSON body:
{
  "symbol": "AAPL",
  "interval": "1min"
}`
2. curl -X 'POST' \
  'http://127.0.0.1:8000/stock-data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "symbol": "AAPL",
  "interval": "1min"
}'
