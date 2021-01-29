import bounceutils
import sys
from bounceutils.core import (execute_query, get_dataframe_from_query)


def executeQuery(query, databaseName, rowsLimit):
    try:
        queryResponse = get_dataframe_from_query(databaseName, query)
        return queryResponse
    except bounceutils.core.config_loader.BounceUtilsConfigError:
        print("Database Name provided doesnt exist")
        sys.exit(1)
    except:
        print("Something went wrong when querying the database")
        sys.exit(1)