terraform {
  backend "remote" {
    hostname = "terraform.schrodinger.com"
    organization = "solutions"

    workspaces {
      name = "TFE_test"
    }
  }
}