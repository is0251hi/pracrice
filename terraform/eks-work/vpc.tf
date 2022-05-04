module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"

  name = "eks-work-VPC"
  cidr = "192.168.0.0/16"

  azs            = ["ap-northeast-1a", "ap-northeast-1c", "ap-northeast-1d"]
  public_subnets = ["192.168.0.0/24", "192.168.1.0/24", "192.168.2.0/24"]
}