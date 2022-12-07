sudo apt-get update
sudo apt-get install -y python3-venv
sudo apt install -y python3-pip

python3 -m venv CS655
. CS655/bin/activate

python -m pip install torch==1.7.0 -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install --upgrade pip
python -m pip install --upgrade pillow
pip install --no-cache-dir install torchvision
pip install flask

git clone https://github.com/leih1219/Geni_Mini_Project.git
