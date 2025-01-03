resource "azurerm_network_interface" "testInterface" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

data "azurerm_image" "packerimage" {
  name                = "linux-test-image"
  resource_group_name = var.resource_group
}

resource "azurerm_linux_virtual_machine" "testVM" {
  name                            = "${var.application_type}-${var.resource_type}"
  location                        = var.location
  resource_group_name             = var.resource_group
  size                            = "Standard_DS2_v2"
  admin_username                  = "adminuser"
  network_interface_ids           = [azurerm_network_interface.testInterface.id]
  admin_password                  = "UdacityAzure2024"
  disable_password_authentication = false
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_id = data.azurerm_image.packerimage.id
}
