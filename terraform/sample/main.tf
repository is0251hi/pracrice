locals {
    INSTANCE_TYPE = "t3.micro"
    REGION = "ap-northeast-1"
    AMI = "ami-06631ebafb3ae5d34"
}

provider "aws" {
    region = local.REGION
}

resource "aws_instance" "example" {
    ami = local.AMI
    instance_type = local.INSTANCE_TYPE
    vpc_security_group_ids = [aws_security_group.example_ec2_group.id]
    tags = {
        Name = "example"
    }
    user_data = <<EOF
        #!/bin/bash
        yum install -y httpd
        sytemctl start httpd.service
    EOF
}


resource "aws_security_group" "example_ec2_group" {
    name = "example_ec2"

    ingress{
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

output "example_instance_id" {
    value = aws_instance.example.id
}
output "pub_dns" {
    value = aws_instance.example.public_dns
}