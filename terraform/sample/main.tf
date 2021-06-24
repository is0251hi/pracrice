resource "aws_instance" "example" {
    ami = "ami-06631ebafb3ae5d34"
    instance_type = "t3.micro"
    tags = {
        Name = "example"
    }
    user_data = <<EOF
        #!/bin/bash
        yum install -y httpd
        sytemctl start httpd.service
    EOF
}