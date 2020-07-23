# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class ProjectArtifacts(dict):
    artifact_identifier: Optional[str] = pulumi.output_property("artifactIdentifier")
    """
    The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
    """
    encryption_disabled: Optional[bool] = pulumi.output_property("encryptionDisabled")
    """
    If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket.
    """
    name: Optional[str] = pulumi.output_property("name")
    """
    The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
    """
    namespace_type: Optional[str] = pulumi.output_property("namespaceType")
    """
    The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
    """
    override_artifact_name: Optional[bool] = pulumi.output_property("overrideArtifactName")
    """
    If set to true, a name specified in the build spec file overrides the artifact name.
    """
    packaging: Optional[str] = pulumi.output_property("packaging")
    """
    The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
    """
    path: Optional[str] = pulumi.output_property("path")
    """
    If `type` is set to `S3`, this is the path to the output artifact
    """
    type: str = pulumi.output_property("type")
    """
    The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectCache(dict):
    location: Optional[str] = pulumi.output_property("location")
    """
    The location where the AWS CodeBuild project stores cached resources. For type `S3` the value must be a valid S3 bucket name/prefix.
    """
    modes: Optional[List[str]] = pulumi.output_property("modes")
    """
    Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
    """
    type: Optional[str] = pulumi.output_property("type")
    """
    The type of storage that will be used for the AWS CodeBuild project cache. Valid values: `NO_CACHE`, `LOCAL`, and `S3`. Defaults to `NO_CACHE`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironment(dict):
    certificate: Optional[str] = pulumi.output_property("certificate")
    """
    The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
    """
    compute_type: str = pulumi.output_property("computeType")
    """
    Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
    """
    environment_variables: Optional[List['outputs.ProjectEnvironmentEnvironmentVariable']] = pulumi.output_property("environmentVariables")
    """
    A set of environment variables to make available to builds for this build project.
    """
    image: str = pulumi.output_property("image")
    """
    The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
    """
    image_pull_credentials_type: Optional[str] = pulumi.output_property("imagePullCredentialsType")
    """
    The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
    """
    privileged_mode: Optional[bool] = pulumi.output_property("privilegedMode")
    """
    If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
    """
    registry_credential: Optional['outputs.ProjectEnvironmentRegistryCredential'] = pulumi.output_property("registryCredential")
    """
    Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
    """
    type: str = pulumi.output_property("type")
    """
    The type of build environment to use for related builds. Available values are: `LINUX_CONTAINER`, `LINUX_GPU_CONTAINER`, `WINDOWS_CONTAINER` or `ARM_CONTAINER`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironmentEnvironmentVariable(dict):
    name: str = pulumi.output_property("name")
    """
    The environment variable's name or key.
    """
    type: Optional[str] = pulumi.output_property("type")
    """
    The type of environment variable. Valid values: `PARAMETER_STORE`, `PLAINTEXT`.
    """
    value: str = pulumi.output_property("value")
    """
    The environment variable's value.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironmentRegistryCredential(dict):
    credential: str = pulumi.output_property("credential")
    """
    The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
    """
    credential_provider: str = pulumi.output_property("credentialProvider")
    """
    The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfig(dict):
    cloudwatch_logs: Optional['outputs.ProjectLogsConfigCloudwatchLogs'] = pulumi.output_property("cloudwatchLogs")
    """
    Configuration for the builds to store logs to CloudWatch
    """
    s3_logs: Optional['outputs.ProjectLogsConfigS3Logs'] = pulumi.output_property("s3Logs")
    """
    Configuration for the builds to store logs to S3.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfigCloudwatchLogs(dict):
    group_name: Optional[str] = pulumi.output_property("groupName")
    """
    The group name of the logs in CloudWatch Logs.
    """
    status: Optional[str] = pulumi.output_property("status")
    """
    Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
    """
    stream_name: Optional[str] = pulumi.output_property("streamName")
    """
    The stream name of the logs in CloudWatch Logs.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfigS3Logs(dict):
    encryption_disabled: Optional[bool] = pulumi.output_property("encryptionDisabled")
    """
    If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket.
    """
    status: Optional[str] = pulumi.output_property("status")
    """
    Current status of logs in CloudWatch Logs for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `ENABLED`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondaryArtifact(dict):
    artifact_identifier: str = pulumi.output_property("artifactIdentifier")
    """
    The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
    """
    encryption_disabled: Optional[bool] = pulumi.output_property("encryptionDisabled")
    """
    If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket. If `path` is not also specified, then `location` can also specify the path of the output artifact in the output bucket.
    """
    name: Optional[str] = pulumi.output_property("name")
    """
    The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
    """
    namespace_type: Optional[str] = pulumi.output_property("namespaceType")
    """
    The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
    """
    override_artifact_name: Optional[bool] = pulumi.output_property("overrideArtifactName")
    """
    If set to true, a name specified in the build spec file overrides the artifact name.
    """
    packaging: Optional[str] = pulumi.output_property("packaging")
    """
    The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
    """
    path: Optional[str] = pulumi.output_property("path")
    """
    If `type` is set to `S3`, this is the path to the output artifact
    """
    type: str = pulumi.output_property("type")
    """
    The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySource(dict):
    auths: Optional[List['outputs.ProjectSecondarySourceAuth']] = pulumi.output_property("auths")
    """
    Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
    """
    buildspec: Optional[str] = pulumi.output_property("buildspec")
    """
    The build spec declaration to use for this build project's related builds.
    """
    git_clone_depth: Optional[float] = pulumi.output_property("gitCloneDepth")
    """
    Truncate git history to this many commits.
    """
    git_submodules_config: Optional['outputs.ProjectSecondarySourceGitSubmodulesConfig'] = pulumi.output_property("gitSubmodulesConfig")
    """
    Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`, `GITHUB` or `GITHUB_ENTERPRISE`.
    """
    insecure_ssl: Optional[bool] = pulumi.output_property("insecureSsl")
    """
    Ignore SSL warnings when connecting to source control.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    The location of the source code from git or s3.
    """
    report_build_status: Optional[bool] = pulumi.output_property("reportBuildStatus")
    """
    Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
    """
    source_identifier: str = pulumi.output_property("sourceIdentifier")
    """
    The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
    """
    type: str = pulumi.output_property("type")
    """
    The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySourceAuth(dict):
    resource: Optional[str] = pulumi.output_property("resource")
    """
    The resource value that applies to the specified authorization type.
    """
    type: str = pulumi.output_property("type")
    """
    The authorization type to use. The only valid value is `OAUTH`
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySourceGitSubmodulesConfig(dict):
    fetch_submodules: bool = pulumi.output_property("fetchSubmodules")
    """
    If set to true, fetches Git submodules for the AWS CodeBuild build project.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSource(dict):
    auths: Optional[List['outputs.ProjectSourceAuth']] = pulumi.output_property("auths")
    """
    Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
    """
    buildspec: Optional[str] = pulumi.output_property("buildspec")
    """
    The build spec declaration to use for this build project's related builds. This must be set when `type` is `NO_SOURCE`.
    """
    git_clone_depth: Optional[float] = pulumi.output_property("gitCloneDepth")
    """
    Truncate git history to this many commits.
    """
    git_submodules_config: Optional['outputs.ProjectSourceGitSubmodulesConfig'] = pulumi.output_property("gitSubmodulesConfig")
    """
    Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`, `GITHUB` or `GITHUB_ENTERPRISE`.
    """
    insecure_ssl: Optional[bool] = pulumi.output_property("insecureSsl")
    """
    Ignore SSL warnings when connecting to source control.
    """
    location: Optional[str] = pulumi.output_property("location")
    """
    The location of the source code from git or s3.
    """
    report_build_status: Optional[bool] = pulumi.output_property("reportBuildStatus")
    """
    Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when the `type` is `BITBUCKET` or `GITHUB`.
    """
    type: str = pulumi.output_property("type")
    """
    The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET`, `S3` or `NO_SOURCE`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSourceAuth(dict):
    resource: Optional[str] = pulumi.output_property("resource")
    """
    The resource value that applies to the specified authorization type.
    """
    type: str = pulumi.output_property("type")
    """
    The authorization type to use. The only valid value is `OAUTH`
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSourceGitSubmodulesConfig(dict):
    fetch_submodules: bool = pulumi.output_property("fetchSubmodules")
    """
    If set to true, fetches Git submodules for the AWS CodeBuild build project.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectVpcConfig(dict):
    security_group_ids: List[str] = pulumi.output_property("securityGroupIds")
    """
    The security group IDs to assign to running builds.
    """
    subnets: List[str] = pulumi.output_property("subnets")
    """
    The subnet IDs within which to run builds.
    """
    vpc_id: str = pulumi.output_property("vpcId")
    """
    The ID of the VPC within which to run builds.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WebhookFilterGroup(dict):
    filters: Optional[List['outputs.WebhookFilterGroupFilter']] = pulumi.output_property("filters")
    """
    A webhook filter for the group. Filter blocks are documented below.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WebhookFilterGroupFilter(dict):
    exclude_matched_pattern: Optional[bool] = pulumi.output_property("excludeMatchedPattern")
    """
    If set to `true`, the specified filter does *not* trigger a build. Defaults to `false`.
    """
    pattern: str = pulumi.output_property("pattern")
    """
    For a filter that uses `EVENT` type, a comma-separated string that specifies one event: `PUSH`, `PULL_REQUEST_CREATED`, `PULL_REQUEST_UPDATED`, `PULL_REQUEST_REOPENED`. `PULL_REQUEST_MERGED` works with GitHub & GitHub Enterprise only. For a filter that uses any of the other filter types, a regular expression.
    """
    type: str = pulumi.output_property("type")
    """
    The webhook filter group's type. Valid values for this parameter are: `EVENT`, `BASE_REF`, `HEAD_REF`, `ACTOR_ACCOUNT_ID`, `FILE_PATH`. At least one filter group must specify `EVENT` as its type.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


