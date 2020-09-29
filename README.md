# kp-test
3 Tier application and challenges

==============
Challenge #1
===============
A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

# gcp-demo-app
Demo App on GCP Cloud Run and deployed using Cloud Build. 

# Deploy CI/CD using Terraform in a GCP Project

Following resources needs to be created.

1. Google Cloud Repository
2. Google Cloud Build
3. Google Cloud Run

Additional steps:
a. Create new GCP Project or select exising project
b. Create Service account(SA) and assign the IAM roles to SA with Editor, Security Admin, Service Usage Consumer, Source Repository Administrator IAM Permissions.
c. Download key as terraform.json or someother file name of your choice
d. Export GOOGLE_CLOUD_KEYFILE_JSON=terraform-admin.json or your desired file name

```
 git clone  https://github.com/rajranganathan/gcp-demo-app.git
 cd  gcp-demo-app/terraform
``` 
<Optional>#### Set Terraform state in Google Cloud Storage if required
export GCP_PROJECT={YOUR_PROJECT_ID}
export TF_STATE=${GCP_PROJECT}-state
gsutil mb -p ${GCP_PROJECT} gs://${TF_STATE}
cat > backend.tf << EOF
terraform {
 backend "gcs" {
   bucket  = "${TF_STATE}"
   prefix  = "terraform/state"
 }
}
EOF
gsutil versioning set on gs://${TF_STATE}
<Optional>

4. terraform init
5. terraform plan
6. terraform apply
7. terraform output url ==> will get url like https://first-app-djzwxcwkza-ew.a.run.app

### Following steps to push the code into Google Cloud Source Repository
1. cd to root directory
2. Set remote
    git remote add google https://source.developers.google.com/p/[PROJECT_ID]/r/[REPO_NAME]
3. Push the code 



==============
Challenge #2
===============
Summary
We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to you. 
Bonus Points
The code allows for a particular data key to be retrieved individually

Solution:
*********
git clone  https://github.com/rajranganathan/kp-test.git
cd kp-test
python3 query_metadata.py


==============
Challenge #3
===============
We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
 
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
 
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a

Solution:
*********
git clone  https://github.com/rajranganathan/kp-test.git
cd kp-test
python3 nested_key_value.py
