# kp-test
Challenges

==============
Challenge #1
===============
A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Solution:
*********
# gcp-demo-app
A Demo Web App and a Python App which retrieves the Entity value for a key from Google Datastore hosted on GCP (Container as a Service) Cloud Run and also automatically deployed using GCP Cloud Build.

Datastore allows entities to be stored in a parent/child relationship. This is known as an entity group or ancestor/descendent relationship.




The entity group has kinds of types person, pet, and toy. The ‘Grandparent’ in this relationship is the ‘Person’. In order to configure this, one must first create the Person entity. Then, a user can create a pet, and specify that the parent is a person key. In order to create the ‘Grandchild’, a user then creates a toy and sets its parent to be a pet key. To further add customisable attributes, a user can specify additional key-value pairs such as age, sex, and type. These key-value pairs are stored as properties and the below solution will use Google Datastore.

In this example, parent key value is retrieved as output for Kind:Pet and Key Pet_id:Cherie from Datastore

# Deploy CI/CD using Terraform in a GCP Project

Following GCP resources needs to be created.

1. Google Cloud Repository
2. Google Cloud Build
3. Google Cloud Run
4. Google Cloud Datastore

Additional steps:
a. Create new GCP Project or select existing project
b. Create Service account(SA) and assign the IAM roles to SA with Editor, Security Admin, Service Usage Consumer, Source Repository Administrator IAM Permissions.
c. Download key as terraform.json or some other file name of your choice
d. Export GOOGLE_CLOUD_KEYFILE_JSON=terraform-admin.json or your desired file name

```
 git clone  https://github.com/rajranganathan/kp-test.git
 cd  kp-test/terraform
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

5. terraform init
6. terraform plan
7. terraform apply
8. terraform output url ==> will get url for DEMO Web App something like https://demo-app-djzwxcwkza-ew.a.run.app
9. This will create GCP Cloud source repository https://source.developers.google.com/p/[PROJECT_ID]/r/[REPO_NAME] as set in terrform.tfvars


### Copy the code into Google Cloud Source Repository
1. cd to root directory of kp-test
2. Copy the contents of "kp-test" directory to GCP Source repository : https://source.developers.google.com/p/[PROJECT_ID]/r/[REPO_NAME]
3. Push the code if there are any more customisable changes.
4. Ensure Google Datastore is enabled


Note the Google Cloud Build will start the automatic CI/CD process and deploy the Application automatically on Google Cloud Run.

Please access the Google Cloud Run URL and you should be able to see the output of Datastore's Entity key value.


==============
Challenge #2
===============
Summary
We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to ]you.
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
