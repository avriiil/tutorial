from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    #FilesystemIOManager,  # Update the imports at the top of the file to also include this
)
from dagster_deltalake import LocalConfig
from dagster_deltalake_pandas import DeltaLakePandasIOManager
from . import assets

all_assets = load_assets_from_modules([assets])

hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

# hackernews_schedule = ScheduleDefinition(
#     job=hackernews_job,
#     cron_schedule="0 * * * *",  # every hour
# )


defs = Definitions(
    assets=all_assets,
    resources={
         "io_manager": DeltaLakePandasIOManager(
             root_uri="/Users/rpelgrim/Desktop/temp",
             storage_options=LocalConfig(),
             schema="dagster_test",
         ),
    },
)
