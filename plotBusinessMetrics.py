import boto3
import json
import createAlarm
import setAnamolyDetectionBand
import createSNStopic
import os
import sys
from pandas import DataFrame


cloudwatch_client=boto3.client('cloudwatch', region_name='ap-south-1')


def cloudwatch(metricsData,namespace,metricName,jobname,email_id):
    print(metricsData)
    AlarmTargetArn=createSNStopic.sns(jobname, namespace, email_id)
    for row in json.loads(metricsData.to_json(orient='records')):
        print(row)
        dimensions=[]
        if metricName not in row.keys():
            print("metricName provided doesn't exist")
            sys.exit(1)

        for column in row:
            print(column)
            print(row[column])
            if column == metricName:
                continue
            dimensions.append({'Name': str(column),'Value': str(row[column])})
        print(dimensions)
        cloudwatch_client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metricName,
                    'Dimensions': dimensions,
                    'Value': row[metricName],
                    'Unit': 'Count',
                },
            ]
        )
        setAnamolyDetectionBand.cloudwatch(namespace, metricName, dimensions)
        createAlarm.cloudwatch(namespace,metricName,dimensions,jobname,email_id,AlarmTargetArn)
