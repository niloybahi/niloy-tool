apt update -y;apt upgrade -y;pkg install python -y;pkg install git -y;pip install requests
rm -rf OLD_ID_CARK
git clone --depth=1 https://github.com/niloybahi/OLD_ID_CARK.git
cd OLD_ID_CARK
git pull
python OLD.py