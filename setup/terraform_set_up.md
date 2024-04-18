## Clone  repository in your local machine. If cloned previously just drive to terraform folder
---
```bash
git clone https://github.com/Okibaba/data-engineering-zoomcamp-project.git
```

```bash
cd data-engineering-zoomcamp-project/terraform
```

## Start up GCP
---
- Initiate terraform and download the required dependencies-

  ```bash
  terraform init
  ```

- View the Terraform plan

  You will be asked to enter the GCP Project ID. Use the same values throughout the project. 

  ```bash
  terraform plan
  ```

- Terraform plan should show the creation of following services

- Apply the infra. **Note** - Billing will start as soon as the apply is complete.

  ```bash
  terraform apply
  ```

- After project is complete you can destroy infrastructure

  ```bash
  terraform destroy
  ```