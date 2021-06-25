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
    tags = {
        Name = "example"
    }
    user_data = <<EOF
        #!/bin/bash
        yum install -y httpd
        sytemctl start httpd.service
    EOF
}

output "example_instance_id" {
    value = aws_instance.example.id
}