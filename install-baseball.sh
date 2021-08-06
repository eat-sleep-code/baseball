# This script will install the Baseball application and any required prerequisites.
cd ~
echo -e ''
echo -e '\033[32mBaseball \033[0m'
echo -e '\033[32m-------------------------------------------------------------------------- \033[0m'
echo -e ''
echo -e '\033[93mUpdating package repositories... \033[0m'
sudo apt update

echo ''
echo -e '\033[93mInstalling prerequisites... \033[0m'
sudo apt install -y git python3 python3-pip libsdl2-image-2.0-0 libsdl2-ttf-2.0-0
sudo pip3 install cairosvg pygame==2.0.1 --force

echo ''
echo -e '\033[93mInstalling Baseball... \033[0m'
cd ~
sudo rm -Rf ~/baseball
sudo git clone https://github.com/eat-sleep-code/baseball
sudo chown -R $USER:$USER baseball
cd baseball
sudo chmod +x baseball.py
mkdir -p images/cache

cd ~
echo ''
echo -e '\033[93mSetting up alias... \033[0m'
sudo touch ~/.bash_aliases
sudo sed -i '/\b\(function baseball\)\b/d' ~/.bash_aliases
sudo sed -i '$ a function baseball { sudo python3 ~/baseball/baseball.py "$@"; }' ~/.bash_aliases
echo -e 'You may use \e[1mbaseball <options>\e[0m to launch the program.'

echo ''
echo -e '\033[32m-------------------------------------------------------------------------- \033[0m'
echo -e '\033[32mInstallation completed. \033[0m'
echo ''
#sudo rm ~/install-baseball.sh
bash
