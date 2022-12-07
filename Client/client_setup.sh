sudo apt-get update
sudo apt-get install -y python3-venv
sudo apt install -y python3-pip

python3 -m venv CS655
. CS655/bin/activate

pip install flask
pip install requests

git clone https://github.com/leih1219/Geni_Mini_Project.git
