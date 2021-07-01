

module "app" {
    source = "./http_server"
}

output "public_dns" {
    value = module.app.public_dns
}