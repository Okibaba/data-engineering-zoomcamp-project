---
Steps to reproduce project
---
 Ensure you have Google cloud account.
To set up and run project, proceed as follows:
- On GCP create a service account with with Google compute engine, Google cloud storage, Google BiqQuery, dataproc with admin previlege
- Create a VM with machine type `n1-standard-1`  Setup the VM following steps at this [link](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13&pp=iAQB):
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
- Install Mage on your VM following instructions [here](https://www.youtube.com/watch?v=tNiV7Wp08XE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=20)
- reproduce  Mage orchestration pipeline as shown below and schedule to run monthly. Use python files in mage-orchestration/data_exporter,mage-orchestration/data_loader, and mage-orchestration/transformer folders.
![Mage orchestration](/screenshots/mage-orchestration/orchestration-flow-diagram-.png)
- once Mage is set up, configure looker visualizaton as shown below
![Project Infrastructure](/screenshots/looker/looker-studio-report.png)
