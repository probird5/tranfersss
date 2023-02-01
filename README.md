# Tranfersss

### Detail

Simple python script to allow you to transfer files via SSH

### Installation

```
git clone https://github.com/probird5/tranfersss.git

cd transfersss

pip3 install -r requirements.txt

python3 transfersss.py 
```

### Usage

```
usage: transfersss.py [-h] [-i HOST] [-f FILE] [-u USERNAME]

options:
  -h, --help            show this help message and exit
  -i HOST, --host HOST  Host you want to transfer a file to.
  -f FILE, --file FILE  The file you want to send
  -u USERNAME, --username USERNAME  User to authenticate as
```

### TODO

- [] add destination file path argument (defaults to the home directory as of now)
- [] add option to use ssh keys
- [] Error handling
