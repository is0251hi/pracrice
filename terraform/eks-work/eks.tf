module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "~> 18.0"
  cluster_name    = "eks-work-cluster"
  cluster_version = "1.21"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.public_subnets
  eks_managed_node_groups = {
    node = {
      min_size       = 2
      max_size       = 5
      desired_size   = 2
      instance_types = ["t2.small"]
      capacity_type  = "SPOT"
      iam_role_additional_policies = [
        "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess",
        "arn:aws:iam::aws:policy/AutoScalingFullAccess",
        "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      ]
    }
  }
}

resource "null_resource" "update_kubeconfig" {
  triggers = {
    cluster_name = module.eks.cluster_id
  }
  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --name ${module.eks.cluster_id}"
  }
  depends_on = [
    module.eks
  ]
}