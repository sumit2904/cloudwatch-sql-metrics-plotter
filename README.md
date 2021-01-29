# Business Metrics Plotter #

Self serve solution to plot data business critial metrics to cloudwatch for alerting. It uses [Data science's data-utils](https://bitbucket.org/wicked-ride/data-utils/src/master/). Refer that repo for the database names.

## Flow Logic ##
 runs query -> plots metrics -> checks if anomaly detection band exists -------> check if alert exists on the metrics -------> exit
                                                                      NO|    Yes                              NO|           Yes
                                                                        |                                       |
                                                                        Create band                             Create Alert
## Necessary Environment Variables ##

* DATABASENAME: The database name used by data utils where the query will be run
* QUERY: Query to be executed which will provide the data
* LIMIT: The number of rows you want to retreive Note: Not yet implementer
* NAMESPACE: The namespace where the metrics will get segregated in cloudwatch
* METRICNAME: The column name whose value has to be plotted in cloudwatch 
* JOBNAME: Name for this alerting job
* EMAIL_ID: Email id to recieve alerts.




### Links ###
* [Architecture and design](docs/ARCHITECTURE.md)
* [API Docs](docs/API.md)