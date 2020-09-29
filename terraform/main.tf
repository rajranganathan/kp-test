# CLOUD SOURCE REPOSITORY - Create Repository
resource "google_sourcerepo_repository" "repo" {
  name       = var.repository_name
  depends_on = [google_project_service.repo]
}

# CLOUD BUILD - Create Build Trigger
resource "google_cloudbuild_trigger" "cloud_build_trigger" {
  name        = var.repository_name
  description = "Cloud Source Repository Trigger ${var.repository_name} (${var.branch_name})"
  trigger_template {
    repo_name   = var.repository_name
    branch_name = var.branch_name
  }

  filename = "cloudbuild.yaml"
  substitutions = {
    _SERVICE_ACCOUNT_EMAIL = google_service_account.sa.email
    _SERVICE_NAME          = var.service_name
    _REGION                = var.region
  }

  depends_on = [google_project_service.build, google_sourcerepo_repository.repo]
}

# CLOUD RUN - Create Service & Expose the Service to the Public
resource "google_cloud_run_service" "my-service" {
  name     = var.service_name
  location = var.region

  template {
    spec {
      containers {
        image = local.image_name
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  depends_on = [google_project_service.run]
}

resource "google_cloud_run_service_iam_member" "allUsers" {
  service  = google_cloud_run_service.my-service.name
  location = google_cloud_run_service.my-service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# Create locals for custom image name
locals {
  image_name = var.image_name == "" ? "${var.region}/gcr.io/${var.project_id}/${var.service_name}" : var.image_name
}
