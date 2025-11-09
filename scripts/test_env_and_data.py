from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables
load_dotenv()

# Fetch values
data_path = os.getenv("DATA_PATH")
random_state = os.getenv("RANDOM_STATE")

print(f"✅ DATA_PATH: {data_path}")
print(f"✅ RANDOM_STATE: {random_state}")

# Check if dataset exists
if os.path.exists(data_path):
    print("✅ Dataset found. Previewing data:")
    df = pd.read_csv(data_path)
    print(df.head())
else:
    print("❌ Dataset not found. Check DATA_PATH in .env file.")
