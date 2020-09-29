terraform {
  required_version = ">= 0.12"

  required_providers {
    # Cloud Run resources were not added until 3.3.0
    google = ">= 3.3"
  }
}
