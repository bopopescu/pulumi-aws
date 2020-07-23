# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class Repository(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the repository
    """
    clone_url_http: pulumi.Output[str] = pulumi.output_property("cloneUrlHttp")
    """
    The URL to use for cloning the repository over HTTPS.
    """
    clone_url_ssh: pulumi.Output[str] = pulumi.output_property("cloneUrlSsh")
    """
    The URL to use for cloning the repository over SSH.
    """
    default_branch: pulumi.Output[Optional[str]] = pulumi.output_property("defaultBranch")
    """
    The default branch of the repository. The branch specified here needs to exist.
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    The description of the repository. This needs to be less than 1000 characters
    """
    repository_id: pulumi.Output[str] = pulumi.output_property("repositoryId")
    """
    The ID of the repository
    """
    repository_name: pulumi.Output[str] = pulumi.output_property("repositoryName")
    """
    The name for the repository. This needs to be less than 100 characters.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, default_branch=None, description=None, repository_name=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a CodeCommit Repository Resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.codecommit.Repository("test",
            description="This is the Sample App Repository",
            repository_name="MyTestRepository")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_branch: The default branch of the repository. The branch specified here needs to exist.
        :param pulumi.Input[str] description: The description of the repository. This needs to be less than 1000 characters
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['default_branch'] = default_branch
            __props__['description'] = description
            if repository_name is None:
                raise TypeError("Missing required property 'repository_name'")
            __props__['repository_name'] = repository_name
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['clone_url_http'] = None
            __props__['clone_url_ssh'] = None
            __props__['repository_id'] = None
        super(Repository, __self__).__init__(
            'aws:codecommit/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, clone_url_http=None, clone_url_ssh=None, default_branch=None, description=None, repository_id=None, repository_name=None, tags=None):
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the repository
        :param pulumi.Input[str] clone_url_http: The URL to use for cloning the repository over HTTPS.
        :param pulumi.Input[str] clone_url_ssh: The URL to use for cloning the repository over SSH.
        :param pulumi.Input[str] default_branch: The default branch of the repository. The branch specified here needs to exist.
        :param pulumi.Input[str] description: The description of the repository. This needs to be less than 1000 characters
        :param pulumi.Input[str] repository_id: The ID of the repository
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["clone_url_http"] = clone_url_http
        __props__["clone_url_ssh"] = clone_url_ssh
        __props__["default_branch"] = default_branch
        __props__["description"] = description
        __props__["repository_id"] = repository_id
        __props__["repository_name"] = repository_name
        __props__["tags"] = tags
        return Repository(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

