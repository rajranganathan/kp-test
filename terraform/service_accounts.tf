# Creating Service Accounts - Create SA
resource "google_service_account" "sa" {
  account_id   = var.service_account_name
  display_name = "A Service Account to access Google Resources"
  depends_on   = [google_project_service.iam]
}
