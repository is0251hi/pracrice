locals{
    INSTANCE_TYPE = "t3.micro"
    REGION = "ap-northeast-1"
}

provider "aws" {
    region = local.REGION
}

data "aws_ami" "recent_amazon_renux_2"{
    most_recent = true
    owners = ["amazon"]

    filter {
        name = "name"
        values = ["amzn2-ami-hvm-2.0.????????-x86_64-gp2"]
    }

    filter {
        name = "state"
        values = ["available"]
    }
}

resource "aws_instance" "sample" {
    ami = data.aws_ami.recent_amazon_renux_2.image_id
    instance_type = local.INSTANCE_TYPE
    user_data = file("./http_server/user_data.sh")
    vpc_security_group_ids = [aws_security_group.app_secure.id]
}

resource "aws_security_group" "app_secure" {
    name = "sample_secure"

    ingress {
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

output "public_dns" {
    value = aws_instance.sample.public_dns
}