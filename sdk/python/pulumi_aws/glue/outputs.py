# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class CatalogTablePartitionKey(dict):
    comment: Optional[str] = pulumi.output_property("comment")
    """
    Free-form text comment.
    """
    name: str = pulumi.output_property("name")
    """
    Name of the SerDe.
    """
    type: Optional[str] = pulumi.output_property("type")
    """
    The datatype of data in the Column.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CatalogTableStorageDescriptor(dict):
    bucket_columns: Optional[List[str]] = pulumi.output_property("bucketColumns")
    """
    A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
    """
    columns: Optional[List['outputs.CatalogTableStorageDescriptorColumn']] = pulumi.output_property("columns")
    """
    A list of the Columns in the table.
    """
    compressed: Optional[bool] = pulumi.output_property("compressed")
    """
    True if the data in the table is compressed, or False if not.
    """
    input_format: Optional[str] = pulumi.output_property("inputFormat")
    """
    The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
    """
    number_of_buckets: Optional[float] = pulumi.output_property("numberOfBuckets")
    """
    Must be specified if the table contains any dimension columns.
    """
    output_format: Optional[str] = pulumi.output_property("outputFormat")
    """
    The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
    """
    parameters: Optional[Dict[str, str]] = pulumi.output_property("parameters")
    """
    A map of initialization parameters for the SerDe, in key-value form.
    """
    ser_de_info: Optional['outputs.CatalogTableStorageDescriptorSerDeInfo'] = pulumi.output_property("serDeInfo")
    """
    Serialization/deserialization (SerDe) information.
    """
    skewed_info: Optional['outputs.CatalogTableStorageDescriptorSkewedInfo'] = pulumi.output_property("skewedInfo")
    """
    Information about values that appear very frequently in a column (skewed values).
    """
    sort_columns: Optional[List['outputs.CatalogTableStorageDescriptorSortColumn']] = pulumi.output_property("sortColumns")
    """
    A list of Order objects specifying the sort order of each bucket in the table.
    """
    stored_as_sub_directories: Optional[bool] = pulumi.output_property("storedAsSubDirectories")
    """
    True if the table data is stored in subdirectories, or False if not.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CatalogTableStorageDescriptorColumn(dict):
    comment: Optional[str] = pulumi.output_property("comment")
    """
    Free-form text comment.
    """
    name: str = pulumi.output_property("name")
    """
    Name of the SerDe.
    """
    type: Optional[str] = pulumi.output_property("type")
    """
    The datatype of data in the Column.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CatalogTableStorageDescriptorSerDeInfo(dict):
    name: Optional[str] = pulumi.output_property("name")
    """
    Name of the SerDe.
    """
    parameters: Optional[Dict[str, str]] = pulumi.output_property("parameters")
    """
    A map of initialization parameters for the SerDe, in key-value form.
    """
    serialization_library: Optional[str] = pulumi.output_property("serializationLibrary")
    """
    Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CatalogTableStorageDescriptorSkewedInfo(dict):
    skewed_column_names: Optional[List[str]] = pulumi.output_property("skewedColumnNames")
    """
    A list of names of columns that contain skewed values.
    """
    skewed_column_value_location_maps: Optional[Dict[str, str]] = pulumi.output_property("skewedColumnValueLocationMaps")
    """
    A list of values that appear so frequently as to be considered skewed.
    """
    skewed_column_values: Optional[List[str]] = pulumi.output_property("skewedColumnValues")
    """
    A map of skewed values to the columns that contain them.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CatalogTableStorageDescriptorSortColumn(dict):
    column: str = pulumi.output_property("column")
    """
    The name of the column.
    """
    sort_order: float = pulumi.output_property("sortOrder")
    """
    Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClassifierCsvClassifier(dict):
    allow_single_column: Optional[bool] = pulumi.output_property("allowSingleColumn")
    """
    Enables the processing of files that contain only one column.
    """
    contains_header: Optional[str] = pulumi.output_property("containsHeader")
    """
    Indicates whether the CSV file contains a header. This can be one of "ABSENT", "PRESENT", or "UNKNOWN".
    """
    delimiter: Optional[str] = pulumi.output_property("delimiter")
    """
    The delimiter used in the Csv to separate columns.
    """
    disable_value_trimming: Optional[bool] = pulumi.output_property("disableValueTrimming")
    """
    Specifies whether to trim column values.
    """
    headers: Optional[List[str]] = pulumi.output_property("headers")
    """
    A list of strings representing column names.
    """
    quote_symbol: Optional[str] = pulumi.output_property("quoteSymbol")
    """
    A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClassifierGrokClassifier(dict):
    classification: str = pulumi.output_property("classification")
    """
    An identifier of the data format that the classifier matches.
    """
    custom_patterns: Optional[str] = pulumi.output_property("customPatterns")
    """
    Custom grok patterns used by this classifier.
    """
    grok_pattern: str = pulumi.output_property("grokPattern")
    """
    The grok pattern used by this classifier.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClassifierJsonClassifier(dict):
    json_path: str = pulumi.output_property("jsonPath")
    """
    A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClassifierXmlClassifier(dict):
    classification: str = pulumi.output_property("classification")
    """
    An identifier of the data format that the classifier matches.
    """
    row_tag: str = pulumi.output_property("rowTag")
    """
    The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ConnectionPhysicalConnectionRequirements(dict):
    availability_zone: Optional[str] = pulumi.output_property("availabilityZone")
    """
    The availability zone of the connection. This field is redundant and implied by `subnet_id`, but is currently an api requirement.
    """
    security_group_id_lists: Optional[List[str]] = pulumi.output_property("securityGroupIdLists")
    """
    The security group ID list used by the connection.
    """
    subnet_id: Optional[str] = pulumi.output_property("subnetId")
    """
    The subnet ID used by the connection.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CrawlerCatalogTarget(dict):
    database_name: str = pulumi.output_property("databaseName")
    """
    The name of the Glue database to be synchronized.
    """
    tables: List[str] = pulumi.output_property("tables")
    """
    A list of catalog tables to be synchronized.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CrawlerDynamodbTarget(dict):
    path: str = pulumi.output_property("path")
    """
    The name of the DynamoDB table to crawl.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CrawlerJdbcTarget(dict):
    connection_name: str = pulumi.output_property("connectionName")
    """
    The name of the connection to use to connect to the JDBC target.
    """
    exclusions: Optional[List[str]] = pulumi.output_property("exclusions")
    """
    A list of glob patterns used to exclude from the crawl.
    """
    path: str = pulumi.output_property("path")
    """
    The path of the JDBC target.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CrawlerS3Target(dict):
    exclusions: Optional[List[str]] = pulumi.output_property("exclusions")
    """
    A list of glob patterns used to exclude from the crawl.
    """
    path: str = pulumi.output_property("path")
    """
    The name of the DynamoDB table to crawl.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CrawlerSchemaChangePolicy(dict):
    delete_behavior: Optional[str] = pulumi.output_property("deleteBehavior")
    """
    The deletion behavior when the crawler finds a deleted object. Valid values: `LOG`, `DELETE_FROM_DATABASE`, or `DEPRECATE_IN_DATABASE`. Defaults to `DEPRECATE_IN_DATABASE`.
    """
    update_behavior: Optional[str] = pulumi.output_property("updateBehavior")
    """
    The update behavior when the crawler finds a changed schema. Valid values: `LOG` or `UPDATE_IN_DATABASE`. Defaults to `UPDATE_IN_DATABASE`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobCommand(dict):
    name: Optional[str] = pulumi.output_property("name")
    """
    The name of the job command. Defaults to `glueetl`. Use `pythonshell` for Python Shell Job Type, `max_capacity` needs to be set if `pythonshell` is chosen.
    """
    python_version: Optional[str] = pulumi.output_property("pythonVersion")
    """
    The Python version being used to execute a Python shell job. Allowed values are 2 or 3.
    """
    script_location: str = pulumi.output_property("scriptLocation")
    """
    Specifies the S3 path to a script that executes a job.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobExecutionProperty(dict):
    max_concurrent_runs: Optional[float] = pulumi.output_property("maxConcurrentRuns")
    """
    The maximum number of concurrent runs allowed for a job. The default is 1.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobNotificationProperty(dict):
    notify_delay_after: Optional[float] = pulumi.output_property("notifyDelayAfter")
    """
    After a job run starts, the number of minutes to wait before sending a job run delay notification.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SecurityConfigurationEncryptionConfiguration(dict):
    cloudwatch_encryption: 'outputs.SecurityConfigurationEncryptionConfigurationCloudwatchEncryption' = pulumi.output_property("cloudwatchEncryption")
    job_bookmarks_encryption: 'outputs.SecurityConfigurationEncryptionConfigurationJobBookmarksEncryption' = pulumi.output_property("jobBookmarksEncryption")
    s3_encryption: 'outputs.SecurityConfigurationEncryptionConfigurationS3Encryption' = pulumi.output_property("s3Encryption")
    """
    A `s3_encryption ` block as described below, which contains encryption configuration for S3 data.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationCloudwatchEncryption(dict):
    cloudwatch_encryption_mode: Optional[str] = pulumi.output_property("cloudwatchEncryptionMode")
    """
    Encryption mode to use for CloudWatch data. Valid values: `DISABLED`, `SSE-KMS`. Default value: `DISABLED`.
    """
    kms_key_arn: Optional[str] = pulumi.output_property("kmsKeyArn")
    """
    Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationJobBookmarksEncryption(dict):
    job_bookmarks_encryption_mode: Optional[str] = pulumi.output_property("jobBookmarksEncryptionMode")
    """
    Encryption mode to use for job bookmarks data. Valid values: `CSE-KMS`, `DISABLED`. Default value: `DISABLED`.
    """
    kms_key_arn: Optional[str] = pulumi.output_property("kmsKeyArn")
    """
    Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationS3Encryption(dict):
    kms_key_arn: Optional[str] = pulumi.output_property("kmsKeyArn")
    """
    Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
    """
    s3_encryption_mode: Optional[str] = pulumi.output_property("s3EncryptionMode")
    """
    Encryption mode to use for S3 data. Valid values: `DISABLED`, `SSE-KMS`, `SSE-S3`. Default value: `DISABLED`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TriggerAction(dict):
    arguments: Optional[Dict[str, str]] = pulumi.output_property("arguments")
    """
    Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
    """
    crawler_name: Optional[str] = pulumi.output_property("crawlerName")
    """
    The name of the crawler to be executed. Conflicts with `job_name`.
    """
    job_name: Optional[str] = pulumi.output_property("jobName")
    """
    The name of a job to be executed. Conflicts with `crawler_name`.
    """
    timeout: Optional[float] = pulumi.output_property("timeout")
    """
    The job run timeout in minutes. It overrides the timeout value of the job.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TriggerPredicate(dict):
    conditions: List['outputs.TriggerPredicateCondition'] = pulumi.output_property("conditions")
    """
    A list of the conditions that determine when the trigger will fire. Defined below.
    """
    logical: Optional[str] = pulumi.output_property("logical")
    """
    How to handle multiple conditions. Defaults to `AND`. Valid values are `AND` or `ANY`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TriggerPredicateCondition(dict):
    crawl_state: Optional[str] = pulumi.output_property("crawlState")
    """
    The condition crawl state. Currently, the values supported are `RUNNING`, `SUCCEEDED`, `CANCELLED`, and `FAILED`. If this is specified, `crawler_name` must also be specified. Conflicts with `state`.
    """
    crawler_name: Optional[str] = pulumi.output_property("crawlerName")
    """
    The name of the crawler to watch. If this is specified, `crawl_state` must also be specified. Conflicts with `job_name`.
    """
    job_name: Optional[str] = pulumi.output_property("jobName")
    """
    The name of the job to watch. If this is specified, `state` must also be specified. Conflicts with `crawler_name`.
    """
    logical_operator: Optional[str] = pulumi.output_property("logicalOperator")
    """
    A logical operator. Defaults to `EQUALS`.
    """
    state: Optional[str] = pulumi.output_property("state")
    """
    The condition job state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`. If this is specified, `job_name` must also be specified. Conflicts with `crawler_state`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetScriptDagEdge(dict):
    source: str = pulumi.output_property("source")
    """
    The ID of the node at which the edge starts.
    """
    target: str = pulumi.output_property("target")
    """
    The ID of the node at which the edge ends.
    """
    target_parameter: Optional[str] = pulumi.output_property("targetParameter")
    """
    The target of the edge.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetScriptDagNode(dict):
    args: List['outputs.GetScriptDagNodeArg'] = pulumi.output_property("args")
    """
    Nested configuration an argument or property of a node. Defined below.
    """
    id: str = pulumi.output_property("id")
    """
    A node identifier that is unique within the node's graph.
    """
    line_number: Optional[float] = pulumi.output_property("lineNumber")
    """
    The line number of the node.
    """
    node_type: str = pulumi.output_property("nodeType")
    """
    The type of node this is.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetScriptDagNodeArg(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the argument or property.
    """
    param: Optional[bool] = pulumi.output_property("param")
    """
    Boolean if the value is used as a parameter. Defaults to `false`.
    """
    value: str = pulumi.output_property("value")
    """
    The value of the argument or property.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


