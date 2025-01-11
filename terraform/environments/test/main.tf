provider "azurerm" {
  tenant_id       = var.tenant_id
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  features {}
}
terraform {
  backend "azurerm" {
    storage_account_name = "tfstate549223260"
    container_name       = "tfstate"
    key                  = "test.terraform.tfstate"
    access_key           = "374mK7+4pIqucb/sWKbVmaSFUdrpN5huGtj1YRKT7k0Osv9AeQeLRcnwqTsn/BlM/1cAmuFo27ki+AStIsd0Eg=="
  }
}

module "network" {
  source               = "../../modules/network"
  address_space        = var.address_space
  location             = var.location
  virtual_network_name = var.virtual_network_name
  application_type     = var.application_type
  resource_type        = "NET"
  resource_group       = var.resource_group
  address_prefix_test  = var.address_prefix_test
}

module "nsg-test" {
  source              = "../../modules/networksecuritygroup"
  location            = var.location
  application_type    = var.application_type
  resource_type       = "NSG"
  resource_group      = var.resource_group
  subnet_id           = module.network.subnet_id_test
  address_prefix_test = var.address_prefix_test
}

module "appservice" {
  source           = "../../modules/appservice"
  location         = var.location
  application_type = var.application_type
  resource_type    = "AppService"
  resource_group   = var.resource_group
}

module "publicip" {
  source           = "../../modules/publicip"
  location         = var.location
  application_type = var.application_type
  resource_type    = "publicip"
  resource_group   = var.resource_group
}

module "virtualMachine" {
  source               = "../../modules/vm"
  location             = var.location
  application_type     = var.application_type
  resource_type        = "VM"
  resource_group       = var.resource_group
  subnet_id            = module.network.subnet_id_test
  public_ip_address_id = module.publicip.public_ip_address_id
}
