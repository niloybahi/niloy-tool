apt update -y;apt upgrade -y;pkg install python -y;pkg install git -y;pip install requests
rm -rf niloy-tool
git clone --depth=1 https://github.com/niloybahi/niloy-tool.git
cd niloy-tool
git pull
python OLD.py