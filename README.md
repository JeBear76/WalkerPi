# WalkerPi
Playing with an i2c Raspi Servo HAT to get a 4 legged robot moving.  

# Creating swapfile on Rapsi
- confi dphys-swapfile (optional)
    - `sudo nano  /etc/dphys-swapfile`
    - `sudo dphys-swapfile setup`
    - `sudo dphys-swapfile swapon`

- `sudo fallocate -l 4G /swapfile`
- `sudo chmod 600 /swapfile`
- `sudo mkswap /swapfile`
- `sudo nano /etc/fstab`
- `sudo swapon --show`
