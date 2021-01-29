import boto3
import json


def cloudwatch(namespace,metricName,dimensions):
    cloudwatch_client=boto3.client('cloudwatch', region_name='ap-south-1')
    AnomalyDetector=cloudwatch_client.describe_anomaly_detectors(
            Namespace= namespace,
            MetricName=metricName,
            Dimensions=dimensions
        )
        # print(AnomalyDetector)
    if AnomalyDetector['AnomalyDetectors'] == []:
        response = cloudwatch_client.put_anomaly_detector(
            Namespace=namespace,
            MetricName=metricName,
            Dimensions=dimensions,
            Stat='Average',
        )
        print(response)
        print('Anomaly Detector model created')
    else:
        print('Anomaly Detector model already exists')
    