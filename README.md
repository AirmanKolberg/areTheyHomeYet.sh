# areTheyHomeYet.sh
A simple and quick way to have your computer notify you whenever your spouse, friend, or any loved one arrives home!  All you need is their IP whenever they're connected to the home router, which can be found with a simple ifconfig, ipconfig, etc.  You can edit this simple script to do anything you'd like upon their arrival (or I suppose their departure), but I thought it would be a fun, little project to see if I could make an application like this.  I hope you all enjoy!

If, for any reason, you would like to donate- though unneccesary, is always apreciated!

BitCoin: 3Gj49JGVPXjw3994bSebQNrHsFJkZE9iRg && Etherium: 0x08b57537943BBb6A527C9c861E9550D9Be9f7729

Thank you all for reading!

# Tips to Configure

Line 14 of 15 in main.py [print('Connected')] is the action to take when the device has connected back to your home IP.  Also, check out devices.py for an idea I had about saving device IP addresses in a dictionary under names.
