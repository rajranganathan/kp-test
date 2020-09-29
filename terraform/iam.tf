# Grant Cloud Build IAM Permissions
data "google_project" "project" {
}

resource "google_project_iam_binding" "binding" {
  members    = ["serviceAccount:${data.google_project.project.number}@cloudbuild.gserviceaccount.com"]
  role       = "roles/run.admin"
  depends_on = [google_project_service.build]
}

resource "google_project_iam_binding" "sa" {
  members    = ["serviceAccount:${data.google_project.project.number}@cloudbuild.gserviceaccount.com"]
  role       = "roles/iam.serviceAccountUser"
  depends_on = [google_project_service.build]
}
