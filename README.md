# data-engineering-zoomcamp-project

## Project summary
In this project we set up a cloud based infrastructure to ingest, process and visualize batch S&P 500 data.
While the data isn't particularly large, my goal for this project was to a scalable demonstrate an end to end data engineering & visualization pipeline. We expect the infrastructure to scale even for larger data set.


## Technologies used
- Terraform - Infrastructure-as-Code (IaC) tool & automatic provisioning of cloud resources; <br>
- Google cloud service - cloud service provider used
- Google Compute Engine - virtual machine <br>
- Google Cloud Storage (GCS) - for data lake storage needs <br>
- Google BigQuery - for  Data Warehouse <br>
- Mage - for orchestration of pipelines <br>
- Spark - for data transformations <br>
- Google Looker studio - for project data visualizations. <br>



![Project Infrastructure](screenshots/mage-orchestration/orchestration-flow-diagram-.png)

pipeline pulls s&p500 data bla-bla

## Report & Discussion
https://lookerstudio.google.com/u/0/reporting/e990566e-53de-42d0-b816-045eb529e9aa/page/cPswD/edit