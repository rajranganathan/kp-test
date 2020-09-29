#Enable API's
resource "google_project_service" "repo" {
  service            = "sourcerepo.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "build" {
  service            = "cloudbuild.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "registry" {
  service            = "containerregistry.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "run" {
  service            = "run.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "iam" {
  service            = "iam.googleapis.com"
  disable_on_destroy = false
}
