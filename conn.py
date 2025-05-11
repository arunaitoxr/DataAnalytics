from sqlalchemy import create_engine
import pandas as pd
import urllib.parse

host = "db.weqtoyuwarqjfdwrzdip.supabase.co"
port = 5432
database = "postgres"
user = "postgres"

actual_password = "Aitoxr@2025@@!"
password = urllib.parse.quote_plus(actual_password)
# Replace this with your actual password

# SQLAlchemy connection string
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")