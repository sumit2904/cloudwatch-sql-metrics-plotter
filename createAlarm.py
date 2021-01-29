import boto3
import json
import os
import sys


def cloudwatch(namespace, metricName, dimensions,jobname,email_id,AlarmTargetArn):
    cloudwatch_client=boto3.client('cloudwatch', region_name='ap-south-1')
    ExistingAlarm=cloudwatch_client.describe_alarms(
            AlarmNames=[jobname+' '+namespace+' Dimensions: '+str(dimensions)+' '+metricName+' Anamoly Alerts'],
            AlarmTypes=['MetricAlarm'],
        )
    if ExistingAlarm['MetricAlarms'] == []:
        response = cloudwatch_client.put_metric_alarm(
            AlarmName=jobname+' '+namespace+' Dimensions: '+str(dimensions)+' '+metricName+' Anamoly Alerts',
            AlarmDescription='Anamoly Alert Triggered by the job - '+jobname+' for the Dimensions - '+str(dimensions)+' for the Namespace - '+namespace,
            ActionsEnabled=True|False,
            # OKActions=[
            #     'string',
            # ],
            AlarmActions=[
                AlarmTargetArn,
            ],
            Metrics=[
                {
                    "Id": "m1",
                    "ReturnData": True,
                    "MetricStat": {
                        "Metric": {
                            "MetricName": metricName,
                            "Namespace": namespace,
                            "Dimensions": dimensions
                        },
                        "Stat": "Average",
                        "Period": 300
                    }
                },
                {
                    "Id": "t1",
                    "Expression": "ANOMALY_DETECTION_BAND(m1, 1.4)"
                }
            ],
            # Period=300,
            # Unit='Count',
            EvaluationPeriods=1,
            #DatapointsToAlarm=1,
            ComparisonOperator='LessThanLowerOrGreaterThanUpperThreshold',
            ThresholdMetricId='t1'
        )
        print('Anomaly detection alarm created')
    else:
        print('Anomaly detection alarm already exists')