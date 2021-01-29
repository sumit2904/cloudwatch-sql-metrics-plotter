import boto3
import json
import os
import sys




def sns(jobname, namespace, email_id):
    sns_client = boto3.client("sns", region_name="ap-south-1")
    sns_paginator = sns_client.get_paginator('list_topics')
    topic_list = sns_paginator.paginate()
    topic_name=str(jobname+'-'+namespace)
    topics = []
    #global topic_arn
    for page in topic_list:
        #print(page)
        for topic in page['Topics']:
            topics.append(topic['TopicArn'])
            #print(topics)
            topic_list=topics
            topic_list=[i.split(':')[-1] for i in topic_list]
    #print(topic_list)
    
        
    if topic_name not in topic_list:
        create_topic=sns_client.create_topic(Name=topic_name)
        topic_arn = create_topic["TopicArn"]
        print("SNS topic is created : %s" % topic_arn)
        subscribe = sns_client.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email_id)
        subscription_arn = subscribe["SubscriptionArn"]
    else:
        for i in topics:
            if i.endswith(topic_name):
                topic_arn=i
        #print(topic_arn)
        print("SNS topic already exists %s" % topic_arn)
        # if topic_name in topics:
        #    topic
    return str(topic_arn)
      
    #print(topics)
    #print(topic_name)

if __name__ == "__main__":  
    sns("test-plotter", "testmetricplotter", "sumit.p@bounceshare.com")

    