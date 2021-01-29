import json
import psycopg2
# import boto3
import mysql.connector
from mysql.connector import Error


# cloudwatch_client = boto3.client('cloudwatch')


class Lambda:

    def postgres_con_test(self, host, database, user, password):
        try:
            conn = psycopg2.connect(host=host, user=user, database=database, password=password, connect_timeout=1)
            conn.close()
            return True
        except:
            return False

    def pg_lambda_handler(self, host, database, user, password, query, sql_fetchmany, metric_name, dimensions_name,
                          unit_name, dimensions_value):

        number_of_selected_col = len(query.split('from')[0].split(','))
        # print("number_of_selected_col {} ".format(number_of_selected_col))
        # print('The host value is: {} The database value is: {} The database '
        #       ' is: {}The password is: {}'.format(host, database, user, password))
        query = query.lower()
        # print('query {}'.format(query))
        conn = psycopg2.connect(host=host, database=database,
                                user=user, password=password)
        cur = conn.cursor()
        cur.execute(query)
        rowcount = cur.rowcount
        # if sql_fetchmany is not None and sql_fetchmany != '' and 0 < sql_fetchmany < 50:
        #     query_data = cur.fetchmany(sql_fetchmany)
        # elif sql_fetchmany > 50 or rowcount>50:
        #     print('Not feasible to run,Too much records has been selected ,Please contact Devops team')
        # else:
        #     query_data = cur.fetchall()
        # print(json.dumps(query_data))
        query_data = cur.fetchmany(sql_fetchmany)
        cur.close()
        for row in query_data:
            # print(row)
            if number_of_selected_col == 2 and (dimensions_value is None or dimensions_value == ''):
                selected_col = row[0]
                agg_col = int(row[1])
                if (selected_col is None) or (selected_col == ""):
                    selected_col = 'None'
                print("MetricName {} ".format(metric_name))
                # cloudwatch_client.put_metric_data(
                #     Namespace='Anomalies',
                #     MetricData=[
                #         {
                #             'MetricName': metric_name,
                #             'Dimensions': [
                #                 {
                #                     'Name': dimensions_name,
                #                     'Value': selected_col
                #                 },
                #             ],
                #             'Value': int(agg_col),
                #             'Unit': unit_name,
                #         },
                #     ]
                # )
                Namespace = 'Anomalies',
                MetricData = [
                    {
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': dimensions_name,
                                'Value': selected_col
                            },
                        ],
                        'Value': int(agg_col),
                        'Unit': unit_name,
                    },
                ]
                print("Namespace {} ".format(Namespace))
                print("MetricData {}".format(MetricData))

            elif number_of_selected_col == 1 and dimensions_value is not None:
                agg_col = int(row[0])
                # cloudwatch_client.put_metric_data(
                #     Namespace='Anomalies',
                #     MetricData=[
                #         {
                #             'MetricName': metric_name,
                #             'Dimensions': [
                #                 {
                #                     'Name': dimensions_name,
                #                     'Value': dimensions_value
                #                 },
                #             ],
                #             'Value': int(agg_col),
                #             'Unit': unit_name,
                #         },
                #     ]
                # )
                Namespace = 'Anomalies',
                MetricData = [
                    {
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': dimensions_name,
                                'Value': dimensions_value
                            },
                        ],
                        'Value': int(agg_col),
                        'Unit': unit_name,
                    },
                ]
                print("Namespace {} ".format(Namespace))
                print("MetricData {}".format(MetricData))

            else:
                print("unexpected error at put_metric_data,Devops team can help")

        return {
            'statusCode': 200,
            'body': json.dumps('Plotted {} to Cloudwatch'.format(dimensions_name))
        }

    def mysql_con_test(self, host, database, user, password):
        conn = None
        try:
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if conn.is_connected():
                print(conn)
                return True

        except Error as e:
            return False
        finally:
            if conn is not None and conn.is_connected():
                conn.close()

    def mysql_lambda_handler(self, host, database, user, password, query, sql_fetchmany, metric_name, dimensions_name,
                             unit_name, dimensions_value):

        number_of_selected_col = len(query.split('from')[0].split(','))
        # print("number_of_selected_col {} ".format(number_of_selected_col))
        # print('The host value is: {} The database value is: {} The database '
        #       ' is: {}The password is: {}'.format(host, database, user, password))
        query = query.lower()
        # print('query {}'.format(query))
        conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
        cur = conn.cursor()
        cur.execute(query)
        rowcount = cur.rowcount
        # if sql_fetchmany is not None and sql_fetchmany != '' and 0 < sql_fetchmany < 50:
        #     query_data = cur.fetchmany(sql_fetchmany)
        # elif sql_fetchmany > 50 or rowcount>50:
        #     print('Not feasible to run,Too much records has been selected ,Please contact Devops team')
        # else:
        #     query_data = cur.fetchall()
        # print(json.dumps(query_data))
        query_data = cur.fetchmany(sql_fetchmany)
        cur.close()
        for row in query_data:
            # print(row)
            if number_of_selected_col == 2 and (dimensions_value is None or dimensions_value == ''):
                selected_col = row[0]
                agg_col = int(row[1])
                if (selected_col is None) or (selected_col == ""):
                    selected_col = 'None'
                print("MetricName {} ".format(metric_name))
                # cloudwatch_client.put_metric_data(
                #     Namespace='Anomalies',
                #     MetricData=[
                #         {
                #             'MetricName': metric_name,
                #             'Dimensions': [
                #                 {
                #                     'Name': dimensions_name,
                #                     'Value': selected_col
                #                 },
                #             ],
                #             'Value': int(agg_col),
                #             'Unit': unit_name,
                #         },
                #     ]
                # )
                Namespace = 'Anomalies',
                MetricData = [
                    {
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': dimensions_name,
                                'Value': selected_col
                            },
                        ],
                        'Value': int(agg_col),
                        'Unit': unit_name,
                    },
                ]
                print("Namespace {} ".format(Namespace))
                print("MetricData {}".format(MetricData))

            elif number_of_selected_col == 1 and dimensions_value is not None:
                agg_col = int(row[0])
                # cloudwatch_client.put_metric_data(
                #     Namespace='Anomalies',
                #     MetricData=[
                #         {
                #             'MetricName': metric_name,
                #             'Dimensions': [
                #                 {
                #                     'Name': dimensions_name,
                #                     'Value': dimensions_value
                #                 },
                #             ],
                #             'Value': int(agg_col),
                #             'Unit': unit_name,
                #         },
                #     ]
                # )
                Namespace = 'Anomalies',
                MetricData = [
                    {
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': dimensions_name,
                                'Value': dimensions_value
                            },
                        ],
                        'Value': int(agg_col),
                        'Unit': unit_name,
                    },
                ]
                print("Namespace {} ".format(Namespace))
                print("MetricData {}".format(MetricData))

            else:
                print("unexpected error at put_metric_data,Devops team can help")

        return {
            'statusCode': 200,
            'body': json.dumps('Plotted {} to Cloudwatch'.format(dimensions_name))
        }
