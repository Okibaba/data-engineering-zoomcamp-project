---
Steps to reproduce project
---
 Ensure you have Google cloud account.
To set up and run project, proceed as follows:
- On GCP create a service account with with Google compute engine, Google cloud storage, Google BiqQuery, dataproc with admin previllage
- Create a VM with machine type `n1-standard-1`  Setup the VM following steps in this [link](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13&pp=iAQB):
    - Install Anaconda using the following steps:
        - Download anaconda using `wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh` or the latest version from this [link](https://www.anaconda.com/download#downloads)
        - `bash Anaconda3-2023.03-1-Linux-x86_64.sh`
    - Install Docker and create a user by using the following steps:
        - `sudo apt-get update`
        - `sudo apt-get install docker.io`
        - `sudo groupadd docker`
        - `sudo gpasswd -a $USER docker` 
        - `sudo docker service restart`

- Install terraform following the instruction in this [link](https://phoenixnap.com/kb/how-to-install-terraform)
- Navigate to the [terraform]() folder, then from your CLI run:
    - `terraform init`
    - `terraform plan`
    - `terraform apply`
- Restart VM 
- Clone this repo using: `git clone https://github.com/Okibaba/data-engineering-zoomcamp-project.git`
- Install Mage following the steps here on your VM following instructions [here]()
- reproduce this Mage steps as shown below and schedule to run monthly. Use python files in mage-orchestration/data_exporter,mage-orchestration/data_loader, and mage-orchestration/transformer folders.
![Mage orchestration](/screenshots/mage-orchestration/orchestration-flow-diagram-.png)
- once Mage is set up, configure looker visualizaton as shown below
![Project Infrastructure](/screenshots/looker/looker-studio-report.png)
