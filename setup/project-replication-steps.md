Reproduce
Prequistes: Ensure you have Google cloud, Mage, to run the project, use the following step:\

On GCP create a service account with with GCE, GCS and BiqQuery admin previllage
Create a VM with machine type n1-standard-1 in europe-west1 region
Setup the VM link:
Install Anaconda using the following steps:
Download anaconda using wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh or the latest version from this link
bash Anaconda3-2023.03-1-Linux-x86_64.sh
Install Docker and create a user by using the following steps:
sudo apt-get update
sudo apt-get install docker.io
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo docker service restart
Restart VM
Clone this repo using: git clone https://github.com/uchiharon/DataTalksClub_de-zoomcamp_CapStone_Project.git
Install terraform following the instruction in this link
Navigate to the 2_terraform folder, then from your CLI run:
terraform init
terraform plan
terraform apply