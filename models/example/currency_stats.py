import pandas as pd
import statistics as stats
from snowflake.snowpark.session import Session

def model(dbt, session: Session):
    df = session.table("PROJECT_SCHEMA.currency").to_pandas()
    df["mean"] = df.apply(lambda row: stats.mean(row), axis=1)
    df["median"] = df.apply(lambda row: stats.median(row), axis=1)
    df["std_dev"] = df.apply(lambda row: stats.stdev(row), axis=1)
    return session.create_dataframe(df)
