# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class CapacityProviderAutoScalingGroupProviderArgs:
    auto_scaling_group_arn: pulumi.Input[str] = pulumi.input_property("autoScalingGroupArn")
    """
    - The Amazon Resource Name (ARN) of the associated auto scaling group.
    """
    managed_scaling: Optional[pulumi.Input['CapacityProviderAutoScalingGroupProviderManagedScalingArgs']] = pulumi.input_property("managedScaling")
    """
    - Nested argument defining the parameters of the auto scaling. Defined below.
    """
    managed_termination_protection: Optional[pulumi.Input[str]] = pulumi.input_property("managedTerminationProtection")
    """
    - Enables or disables container-aware termination of instances in the auto scaling group when scale-in happens. Valid values are `ENABLED` and `DISABLED`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, auto_scaling_group_arn: pulumi.Input[str], managed_scaling: Optional[pulumi.Input['CapacityProviderAutoScalingGroupProviderManagedScalingArgs']] = None, managed_termination_protection: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] auto_scaling_group_arn: - The Amazon Resource Name (ARN) of the associated auto scaling group.
        :param pulumi.Input['CapacityProviderAutoScalingGroupProviderManagedScalingArgs'] managed_scaling: - Nested argument defining the parameters of the auto scaling. Defined below.
        :param pulumi.Input[str] managed_termination_protection: - Enables or disables container-aware termination of instances in the auto scaling group when scale-in happens. Valid values are `ENABLED` and `DISABLED`.
        """
        __self__.auto_scaling_group_arn = auto_scaling_group_arn
        __self__.managed_scaling = managed_scaling
        __self__.managed_termination_protection = managed_termination_protection

@pulumi.input_type
class CapacityProviderAutoScalingGroupProviderManagedScalingArgs:
    maximum_scaling_step_size: Optional[pulumi.Input[float]] = pulumi.input_property("maximumScalingStepSize")
    """
    The maximum step adjustment size. A number between 1 and 10,000.
    """
    minimum_scaling_step_size: Optional[pulumi.Input[float]] = pulumi.input_property("minimumScalingStepSize")
    """
    The minimum step adjustment size. A number between 1 and 10,000.
    """
    status: Optional[pulumi.Input[str]] = pulumi.input_property("status")
    """
    Whether auto scaling is managed by ECS. Valid values are `ENABLED` and `DISABLED`.
    """
    target_capacity: Optional[pulumi.Input[float]] = pulumi.input_property("targetCapacity")
    """
    The target utilization for the capacity provider. A number between 1 and 100.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, maximum_scaling_step_size: Optional[pulumi.Input[float]] = None, minimum_scaling_step_size: Optional[pulumi.Input[float]] = None, status: Optional[pulumi.Input[str]] = None, target_capacity: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[float] maximum_scaling_step_size: The maximum step adjustment size. A number between 1 and 10,000.
        :param pulumi.Input[float] minimum_scaling_step_size: The minimum step adjustment size. A number between 1 and 10,000.
        :param pulumi.Input[str] status: Whether auto scaling is managed by ECS. Valid values are `ENABLED` and `DISABLED`.
        :param pulumi.Input[float] target_capacity: The target utilization for the capacity provider. A number between 1 and 100.
        """
        __self__.maximum_scaling_step_size = maximum_scaling_step_size
        __self__.minimum_scaling_step_size = minimum_scaling_step_size
        __self__.status = status
        __self__.target_capacity = target_capacity

@pulumi.input_type
class ClusterDefaultCapacityProviderStrategyArgs:
    capacity_provider: pulumi.Input[str] = pulumi.input_property("capacityProvider")
    """
    The short name of the capacity provider.
    """
    base: Optional[pulumi.Input[float]] = pulumi.input_property("base")
    """
    The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
    """
    weight: Optional[pulumi.Input[float]] = pulumi.input_property("weight")
    """
    The relative percentage of the total number of launched tasks that should use the specified capacity provider.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, capacity_provider: pulumi.Input[str], base: Optional[pulumi.Input[float]] = None, weight: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] capacity_provider: The short name of the capacity provider.
        :param pulumi.Input[float] base: The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
        :param pulumi.Input[float] weight: The relative percentage of the total number of launched tasks that should use the specified capacity provider.
        """
        __self__.capacity_provider = capacity_provider
        __self__.base = base
        __self__.weight = weight

@pulumi.input_type
class ClusterSettingArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    Name of the setting to manage. Valid values: `containerInsights`.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The value to assign to the setting. Value values are `enabled` and `disabled`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], value: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] name: Name of the setting to manage. Valid values: `containerInsights`.
        :param pulumi.Input[str] value: The value to assign to the setting. Value values are `enabled` and `disabled`.
        """
        __self__.name = name
        __self__.value = value

@pulumi.input_type
class ServiceCapacityProviderStrategyArgs:
    capacity_provider: pulumi.Input[str] = pulumi.input_property("capacityProvider")
    """
    The short name of the capacity provider.
    """
    base: Optional[pulumi.Input[float]] = pulumi.input_property("base")
    """
    The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
    """
    weight: Optional[pulumi.Input[float]] = pulumi.input_property("weight")
    """
    The relative percentage of the total number of launched tasks that should use the specified capacity provider.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, capacity_provider: pulumi.Input[str], base: Optional[pulumi.Input[float]] = None, weight: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] capacity_provider: The short name of the capacity provider.
        :param pulumi.Input[float] base: The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
        :param pulumi.Input[float] weight: The relative percentage of the total number of launched tasks that should use the specified capacity provider.
        """
        __self__.capacity_provider = capacity_provider
        __self__.base = base
        __self__.weight = weight

@pulumi.input_type
class ServiceDeploymentControllerArgs:
    type: Optional[pulumi.Input[str]] = pulumi.input_property("type")
    """
    Type of deployment controller. Valid values: `CODE_DEPLOY`, `ECS`, `EXTERNAL`. Default: `ECS`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, type: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] type: Type of deployment controller. Valid values: `CODE_DEPLOY`, `ECS`, `EXTERNAL`. Default: `ECS`.
        """
        __self__.type = type

@pulumi.input_type
class ServiceLoadBalancerArgs:
    container_name: pulumi.Input[str] = pulumi.input_property("containerName")
    """
    The name of the container to associate with the load balancer (as it appears in a container definition).
    """
    container_port: pulumi.Input[float] = pulumi.input_property("containerPort")
    """
    The port on the container to associate with the load balancer.
    """
    elb_name: Optional[pulumi.Input[str]] = pulumi.input_property("elbName")
    """
    The name of the ELB (Classic) to associate with the service.
    """
    target_group_arn: Optional[pulumi.Input[str]] = pulumi.input_property("targetGroupArn")
    """
    The ARN of the Load Balancer target group to associate with the service.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, container_name: pulumi.Input[str], container_port: pulumi.Input[float], elb_name: Optional[pulumi.Input[str]] = None, target_group_arn: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] container_name: The name of the container to associate with the load balancer (as it appears in a container definition).
        :param pulumi.Input[float] container_port: The port on the container to associate with the load balancer.
        :param pulumi.Input[str] elb_name: The name of the ELB (Classic) to associate with the service.
        :param pulumi.Input[str] target_group_arn: The ARN of the Load Balancer target group to associate with the service.
        """
        __self__.container_name = container_name
        __self__.container_port = container_port
        __self__.elb_name = elb_name
        __self__.target_group_arn = target_group_arn

@pulumi.input_type
class ServiceNetworkConfigurationArgs:
    subnets: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("subnets")
    """
    The subnets associated with the task or service.
    """
    assign_public_ip: Optional[pulumi.Input[bool]] = pulumi.input_property("assignPublicIp")
    """
    Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
    """
    security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("securityGroups")
    """
    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, subnets: pulumi.Input[List[pulumi.Input[str]]], assign_public_ip: Optional[pulumi.Input[bool]] = None, security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: The subnets associated with the task or service.
        :param pulumi.Input[bool] assign_public_ip: Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
        """
        __self__.subnets = subnets
        __self__.assign_public_ip = assign_public_ip
        __self__.security_groups = security_groups

@pulumi.input_type
class ServiceOrderedPlacementStrategyArgs:
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    The type of placement strategy. Must be one of: `binpack`, `random`, or `spread`
    """
    field: Optional[pulumi.Input[str]] = pulumi.input_property("field")
    """
    For the `spread` placement strategy, valid values are `instanceId` (or `host`,
    which has the same effect), or any platform or custom attribute that is applied to a container instance.
    For the `binpack` type, valid values are `memory` and `cpu`. For the `random` type, this attribute is not
    needed. For more information, see [Placement Strategy](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementStrategy.html).
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, type: pulumi.Input[str], field: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] type: The type of placement strategy. Must be one of: `binpack`, `random`, or `spread`
        :param pulumi.Input[str] field: For the `spread` placement strategy, valid values are `instanceId` (or `host`,
               which has the same effect), or any platform or custom attribute that is applied to a container instance.
               For the `binpack` type, valid values are `memory` and `cpu`. For the `random` type, this attribute is not
               needed. For more information, see [Placement Strategy](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementStrategy.html).
        """
        __self__.type = type
        __self__.field = field

@pulumi.input_type
class ServicePlacementConstraintArgs:
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    The type of constraint. The only valid values at this time are `memberOf` and `distinctInstance`.
    """
    expression: Optional[pulumi.Input[str]] = pulumi.input_property("expression")
    """
    Cluster Query Language expression to apply to the constraint. Does not need to be specified
    for the `distinctInstance` type.
    For more information, see [Cluster Query Language in the Amazon EC2 Container
    Service Developer
    Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, type: pulumi.Input[str], expression: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] type: The type of constraint. The only valid values at this time are `memberOf` and `distinctInstance`.
        :param pulumi.Input[str] expression: Cluster Query Language expression to apply to the constraint. Does not need to be specified
               for the `distinctInstance` type.
               For more information, see [Cluster Query Language in the Amazon EC2 Container
               Service Developer
               Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
        """
        __self__.type = type
        __self__.expression = expression

@pulumi.input_type
class ServiceServiceRegistriesArgs:
    registry_arn: pulumi.Input[str] = pulumi.input_property("registryArn")
    """
    The ARN of the Service Registry. The currently supported service registry is Amazon Route 53 Auto Naming Service(`servicediscovery.Service`). For more information, see [Service](https://docs.aws.amazon.com/Route53/latest/APIReference/API_autonaming_Service.html)
    """
    container_name: Optional[pulumi.Input[str]] = pulumi.input_property("containerName")
    """
    The container name value, already specified in the task definition, to be used for your service discovery service.
    """
    container_port: Optional[pulumi.Input[float]] = pulumi.input_property("containerPort")
    """
    The port value, already specified in the task definition, to be used for your service discovery service.
    """
    port: Optional[pulumi.Input[float]] = pulumi.input_property("port")
    """
    The port value used if your Service Discovery service specified an SRV record.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, registry_arn: pulumi.Input[str], container_name: Optional[pulumi.Input[str]] = None, container_port: Optional[pulumi.Input[float]] = None, port: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] registry_arn: The ARN of the Service Registry. The currently supported service registry is Amazon Route 53 Auto Naming Service(`servicediscovery.Service`). For more information, see [Service](https://docs.aws.amazon.com/Route53/latest/APIReference/API_autonaming_Service.html)
        :param pulumi.Input[str] container_name: The container name value, already specified in the task definition, to be used for your service discovery service.
        :param pulumi.Input[float] container_port: The port value, already specified in the task definition, to be used for your service discovery service.
        :param pulumi.Input[float] port: The port value used if your Service Discovery service specified an SRV record.
        """
        __self__.registry_arn = registry_arn
        __self__.container_name = container_name
        __self__.container_port = container_port
        __self__.port = port

@pulumi.input_type
class TaskDefinitionInferenceAcceleratorArgs:
    device_name: pulumi.Input[str] = pulumi.input_property("deviceName")
    """
    The Elastic Inference accelerator device name. The deviceName must also be referenced in a container definition as a ResourceRequirement.
    """
    device_type: pulumi.Input[str] = pulumi.input_property("deviceType")
    """
    The Elastic Inference accelerator type to use.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, device_name: pulumi.Input[str], device_type: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] device_name: The Elastic Inference accelerator device name. The deviceName must also be referenced in a container definition as a ResourceRequirement.
        :param pulumi.Input[str] device_type: The Elastic Inference accelerator type to use.
        """
        __self__.device_name = device_name
        __self__.device_type = device_type

@pulumi.input_type
class TaskDefinitionPlacementConstraintArgs:
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
    """
    expression: Optional[pulumi.Input[str]] = pulumi.input_property("expression")
    """
    Cluster Query Language expression to apply to the constraint.
    For more information, see [Cluster Query Language in the Amazon EC2 Container
    Service Developer
    Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, type: pulumi.Input[str], expression: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] type: The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
        :param pulumi.Input[str] expression: Cluster Query Language expression to apply to the constraint.
               For more information, see [Cluster Query Language in the Amazon EC2 Container
               Service Developer
               Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
        """
        __self__.type = type
        __self__.expression = expression

@pulumi.input_type
class TaskDefinitionProxyConfigurationArgs:
    container_name: pulumi.Input[str] = pulumi.input_property("containerName")
    """
    The name of the container that will serve as the App Mesh proxy.
    """
    properties: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("properties")
    """
    The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
    """
    type: Optional[pulumi.Input[str]] = pulumi.input_property("type")
    """
    The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, container_name: pulumi.Input[str], properties: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, type: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] container_name: The name of the container that will serve as the App Mesh proxy.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] properties: The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
        :param pulumi.Input[str] type: The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
        """
        __self__.container_name = container_name
        __self__.properties = properties
        __self__.type = type

@pulumi.input_type
class TaskDefinitionVolumeArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The name of the volume. This name is referenced in the `sourceVolume`
    parameter of container definition in the `mountPoints` section.
    """
    docker_volume_configuration: Optional[pulumi.Input['TaskDefinitionVolumeDockerVolumeConfigurationArgs']] = pulumi.input_property("dockerVolumeConfiguration")
    """
    Used to configure a docker volume
    """
    efs_volume_configuration: Optional[pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationArgs']] = pulumi.input_property("efsVolumeConfiguration")
    """
    Used to configure a EFS volume.
    """
    host_path: Optional[pulumi.Input[str]] = pulumi.input_property("hostPath")
    """
    The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], docker_volume_configuration: Optional[pulumi.Input['TaskDefinitionVolumeDockerVolumeConfigurationArgs']] = None, efs_volume_configuration: Optional[pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationArgs']] = None, host_path: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] name: The name of the volume. This name is referenced in the `sourceVolume`
               parameter of container definition in the `mountPoints` section.
        :param pulumi.Input['TaskDefinitionVolumeDockerVolumeConfigurationArgs'] docker_volume_configuration: Used to configure a docker volume
        :param pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationArgs'] efs_volume_configuration: Used to configure a EFS volume.
        :param pulumi.Input[str] host_path: The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
        """
        __self__.name = name
        __self__.docker_volume_configuration = docker_volume_configuration
        __self__.efs_volume_configuration = efs_volume_configuration
        __self__.host_path = host_path

@pulumi.input_type
class TaskDefinitionVolumeDockerVolumeConfigurationArgs:
    autoprovision: Optional[pulumi.Input[bool]] = pulumi.input_property("autoprovision")
    """
    If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
    """
    driver: Optional[pulumi.Input[str]] = pulumi.input_property("driver")
    """
    The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
    """
    driver_opts: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("driverOpts")
    """
    A map of Docker driver specific options.
    """
    labels: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("labels")
    """
    A map of custom metadata to add to your Docker volume.
    """
    scope: Optional[pulumi.Input[str]] = pulumi.input_property("scope")
    """
    The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, autoprovision: Optional[pulumi.Input[bool]] = None, driver: Optional[pulumi.Input[str]] = None, driver_opts: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, labels: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, scope: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[bool] autoprovision: If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
        :param pulumi.Input[str] driver: The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] driver_opts: A map of Docker driver specific options.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] labels: A map of custom metadata to add to your Docker volume.
        :param pulumi.Input[str] scope: The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
        """
        __self__.autoprovision = autoprovision
        __self__.driver = driver
        __self__.driver_opts = driver_opts
        __self__.labels = labels
        __self__.scope = scope

@pulumi.input_type
class TaskDefinitionVolumeEfsVolumeConfigurationArgs:
    file_system_id: pulumi.Input[str] = pulumi.input_property("fileSystemId")
    """
    The ID of the EFS File System.
    """
    authorization_config: Optional[pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs']] = pulumi.input_property("authorizationConfig")
    """
    The authorization configuration details for the Amazon EFS file system.
    """
    root_directory: Optional[pulumi.Input[str]] = pulumi.input_property("rootDirectory")
    """
    The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying / will have the same effect as omitting this parameter. This argument is ignored when using `authorization_config`.
    """
    transit_encryption: Optional[pulumi.Input[str]] = pulumi.input_property("transitEncryption")
    """
    Whether or not to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. Valid values: `ENABLED`, `DISABLED`. If this parameter is omitted, the default value of `DISABLED` is used.
    """
    transit_encryption_port: Optional[pulumi.Input[float]] = pulumi.input_property("transitEncryptionPort")
    """
    The port to use for transit encryption. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, file_system_id: pulumi.Input[str], authorization_config: Optional[pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs']] = None, root_directory: Optional[pulumi.Input[str]] = None, transit_encryption: Optional[pulumi.Input[str]] = None, transit_encryption_port: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] file_system_id: The ID of the EFS File System.
        :param pulumi.Input['TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs'] authorization_config: The authorization configuration details for the Amazon EFS file system.
        :param pulumi.Input[str] root_directory: The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying / will have the same effect as omitting this parameter. This argument is ignored when using `authorization_config`.
        :param pulumi.Input[str] transit_encryption: Whether or not to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. Valid values: `ENABLED`, `DISABLED`. If this parameter is omitted, the default value of `DISABLED` is used.
        :param pulumi.Input[float] transit_encryption_port: The port to use for transit encryption. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses.
        """
        __self__.file_system_id = file_system_id
        __self__.authorization_config = authorization_config
        __self__.root_directory = root_directory
        __self__.transit_encryption = transit_encryption
        __self__.transit_encryption_port = transit_encryption_port

@pulumi.input_type
class TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs:
    access_point_id: Optional[pulumi.Input[str]] = pulumi.input_property("accessPointId")
    """
    The access point ID to use. If an access point is specified, the root directory value will be relative to the directory set for the access point. If specified, transit encryption must be enabled in the EFSVolumeConfiguration.
    """
    iam: Optional[pulumi.Input[str]] = pulumi.input_property("iam")
    """
    Whether or not to use the Amazon ECS task IAM role defined in a task definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the EFSVolumeConfiguration. Valid values: `ENABLED`, `DISABLED`. If this parameter is omitted, the default value of `DISABLED` is used.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, access_point_id: Optional[pulumi.Input[str]] = None, iam: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] access_point_id: The access point ID to use. If an access point is specified, the root directory value will be relative to the directory set for the access point. If specified, transit encryption must be enabled in the EFSVolumeConfiguration.
        :param pulumi.Input[str] iam: Whether or not to use the Amazon ECS task IAM role defined in a task definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the EFSVolumeConfiguration. Valid values: `ENABLED`, `DISABLED`. If this parameter is omitted, the default value of `DISABLED` is used.
        """
        __self__.access_point_id = access_point_id
        __self__.iam = iam

