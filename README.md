# PyFileEncrypt

## Introduction

PyFileEncrypt is a set of **Python Scripts** that can help you encrypt files such as images and videos, with the `AES 256 Encryption Algorithm`

The **Python Scripts** uses **External Libraries** including <a href="https://github.com/marcobellaccini/pyAesCrypt">pyAesCrypt</a> and <a href="https://github.com/asweigart/stdiomask">stdiomask</a>

## Usage

Since PyFileEncrypt uses **External Libraries**, you have to install the **Libraries** before using the **Scripts**

### To install with pip, run:

```shell
pip install pyAesCrypt
```

#### And

```shell
pip install stdiomask
```

### To use the scripts, run:

##### Encrypt:

```shell
python3 FileEncrypt.py
```

##### Decrypt:

```shell
python3 FileDecrypt.py
```



## Example

```shell
mctvr@MCTVR % python3 FileEncrypt.py
Input your filename here (same dir with extension): mastercreeper.png
Password: ********
Progress: 0%
Progress: 60%
Progress: 80%
Progress: 100%
mctvr@MCTVR % 
```

``` shell
mctvr@MCTVR % python3 FileDecrypt.py   
Input your filename here (same dir with .pyenc): mastercreeper.png.pyenc
Password: ********
Progress: 0%
Progress: 20%
Progress: 60%
Progress: 100%
mctvr@MCTVR % 
```
