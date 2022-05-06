resource "aws_ecr_repository" "backend" {
  name                 = "k8sbook/backend-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_repository" "batch" {
  name                 = "k8sbook/batch-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}