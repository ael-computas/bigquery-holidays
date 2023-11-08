import holidays
import pyarrow as pa
import pyarrow.parquet as pq
from smart_open import open

BASE_PATH = "gs://ael-holidays"

schema = pa.schema([
    ('country', pa.string()),
    ('name', pa.string()),
    ('date', pa.date32()),
])

for year in range(1900, 2050):
    batches = []
    for code in holidays.list_localized_countries():

        print("{}".format(code))
        try:
            h = holidays.country_holidays(country=code, years=[year], expand=True, language="en_US")
            country = []
            names = []
            dates = []

            for date, name in sorted(h.items()):
                country.append(code)
                names.append(name)
                dates.append(date)
                print("    {} {}".format(date, name))
            batches.append(pa.RecordBatch.from_arrays([country, names, dates], schema=schema))
        except Exception as e:
            print(f"{e}")
    table = pa.Table.from_batches(batches)
    with open(f'{BASE_PATH}/holidays-{year}.parquet', 'wb') as f:
        pq.write_table(table, f)

