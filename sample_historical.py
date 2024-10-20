from openchart import NSEData
import datetime

# Initialize the NSEData class
nse = NSEData()

# Download master data for NSE and NFO
nse.download()

# Define the start and end dates (last 30 days)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)

# Fetch 5-minute historical data for RELIANCE
data = nse.historical(
    symbol='RELIANCE',
    exchange='NSE',
    start=start_date,
    end=end_date,
    interval='5m'
)

# Display the fetched data
if not data.empty:
    print("5-minute historical data for RELIANCE (Last 30 days):")
    print(data)
else:
    print("No data available for RELIANCE for the specified time period.")