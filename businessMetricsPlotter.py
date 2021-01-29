import os
import sys
import json
import getBusinessMetrics
import plotBusinessMetrics

# metric_name = os.environ.get('METRIC_NAME')
# dimensions_name = os.environ.get('DIMENSIONS_NAME')
# dimensions_value = os.environ.get('DIMENSIONS_VALUE')
# unit_name = os.environ.get('UNIT_NAME')

if os.environ.get('DATABASENAME') is not None:
    databaseName=os.environ.get('DATABASENAME')
else:
    print("DATABASENAME is not provided")
    sys.exit(1) 

if os.environ.get('QUERY') is not None:
    query=os.environ.get('QUERY')
else:
    print("QUERY is not provided")
    sys.exit(1)    

if os.environ.get('LIMIT') is not None:
    rowsLimit=os.environ.get('LIMIT')
else:
    print("LIMIT is not provided")
    sys.exit(1)   

if os.environ.get('NAMESPACE') is not None:
    namespace=os.environ.get('NAMESPACE')
else:
    print("NAMESPACE is not provided")
    sys.exit(1) 

if os.environ.get('METRICNAME') is not None:
    metricName=os.environ.get('METRICNAME')
else:
    print("METRICNAME is not provided")
    sys.exit(1) 

if os.environ.get('EMAIL_ID') is not None:
    email_id=os.environ.get('EMAIL_ID')
else:
    print("EMAIL_ID is not provided")
    sys.exit(1) 

if os.environ.get('JOBNAME') is not None:
    jobname=os.environ.get('JOBNAME')
else:
    print("JOBNAME is not provided")
    sys.exit(1) 

metricsData=getBusinessMetrics.executeQuery(query, databaseName, rowsLimit)
plotBusinessMetrics.cloudwatch(metricsData,namespace,metricName,jobname,email_id)

sys.exit(0)


