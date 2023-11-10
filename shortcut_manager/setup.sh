#!/bin/bash

# Move the entire directory to a system directory
sudo cp shortcut.sh /usr/local/bin/shortcut
sudo cp shortcut_manager.py /usr/local/bin/shortcut_manager.py
sudo cp shortcuts.json /usr/local/bin/shortcuts.json

#Managing file permissions
sudo chmod +x /usr/local/bin/shortcut
sudo chmod a+rw /usr/local/bin/shortcuts.json

# Add /usr/local/bin to system PATH variable to enable running command from any directory
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc

echo "Setup completed successfully!"

