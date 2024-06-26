# data-engineering-zoomcamp-project
# S&P500 trading volume data analysis & shock detection

## Project summary
In this data engineering project, we set up a cloud based batch data pipeline to ingest, process and visualize S&P 500 data. The Standard and Poor's 500 or S&P 500 is the most famous financial benchmark in the world. This stock market index tracks the performance of 500 large companies listed on stock exchanges in the United States.

Goal of analysis was to understand volume trend for the S&P500 from 2010 to present. One interesting use of this type of analysis is to understand market anomalies and shocks. During shock periods (say a crash) the volume traded in the market tends to spike and displays an outlier behavior. Of course there are more rigorous analysis to study shocks in the market, but that's outside the scope of project, here we take a simple approach which can be built upon later on.

While the data isn't particularly large, my goal for this project was to demonstrate building a scalable end to end data engineering & visualization pipeline thereby practicing & curating knowledge & skills acquired from the data engineering zoomcamp program so far, also I need this to get the course certificate! 


## Technologies used
- Terraform - Infrastructure-as-Code (IaC) tool & automatic provisioning of cloud resources; <br>
- Docker & Docker-compose- containerization <br>
- Google cloud service - cloud service provider used <br>
- Google Compute Engine - virtual machine <br>
- Google Cloud Storage (GCS) - data lake storage needs <br>
- Google BigQuery -  data Warehouse <br>
- Spark -  data transformations <br>
- Google Looker studio - data visualizations. <br>
- Mage - orchestration of batch pipeline <br>


## Project architecture

![Project Infrastructure](screenshots/project-architecture-design-flow.png)

## Mage orchestration/pipeline
Mage pipeline is show below, pipeline is scheduled to run monthly.
![Project Infrastructure](screenshots/mage-orchestration/orchestration-flow-diagram-.png)

## Data source and schema
We use kaggle S&P500 data which can be found here:
https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks

Data columns & types are as follows: <br>
-'Date':datetime <br>
-'Symbol':str <br>
-'Adj Close':float <br>
-'Close':float <br>
-'Adj Close':float <br>
-'High':float <br>
-'Low':float <br>
-'Open':float <br>
-'Volume': pd.Int64Dtype() <br>



## Report & Discussion
### looker report link
https://lookerstudio.google.com/u/0/reporting/e990566e-53de-42d0-b816-045eb529e9aa/page/cPswD/edit

![Project Infrastructure](screenshots/looker/looker-studio-report.png)

## key findings from analysis
-Apple appears to be one of the most traded S&P500 stock. <br>
-We can see peak volume trends around 2010 during the global financial crisis. <br>
-In general the maximum volume traded over time seems to have dropped which is a bit interesting or could just be a due to data processing artefact, and might warrant further investigation. <br>

## Future work
These are some ideas I plan to explore in future: <br>
-redo project but using a streaming data source <br>
-expand on spark pipeline <br>
-extend analysis and potentially use machine learning to predict onset of market shocks <br>
-edit visualization to allow for filtering <br>
-implement tests, makefiles & CI/CD pipelines <br>

## Reproduce project?

Please check tutorial [here](setup/project-replication-steps.md) to reproduce project

## References
https://github.com/sanyassyed/sf_eviction/blob/master/Makefile
https://github.com/uchiharon/DataTalksClub_de-zoomcamp_CapStone_Project
https://github.com/DataTalksClub/data-engineering-zoomcamp


