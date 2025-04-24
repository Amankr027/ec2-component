import pulumi
import pulumi_aws as aws

class Ec2WithSecurityGroup(pulumi.ComponentResource):
    def __init__(self, name: str, ami_id: str, instance_type: str, opts=None):
        super().__init__('custom:resource:Ec2WithSecurityGroup', name, {}, opts)

        sg = aws.ec2.SecurityGroup(f"{name}-sg",
            description="Allow SSH",
            ingress=[{
                "protocol": "tcp",
                "from_port": 22,
                "to_port": 22,
                "cidr_blocks": ["0.0.0.0/0"],
            }],
            egress=[{
                "protocol": "-1",
                "from_port": 0,
                "to_port": 0,
                "cidr_blocks": ["0.0.0.0/0"],
            }],
            opts=pulumi.ResourceOptions(parent=self)
        )

        instance = aws.ec2.Instance(f"{name}-instance",
            ami=ami_id,
            instance_type=instance_type,
            vpc_security_group_ids=[sg.id],
            tags={"Name": f"{name}-ec2"},
            opts=pulumi.ResourceOptions(parent=self)
        )

        self.instance_id = instance.id
        self.register_outputs({"instance_id": self.instance_id})
