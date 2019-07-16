## XXE

### Pre Requisites
* Docker

### Install Docker
[Docker Link](https://docs.docker.com/install/linux/docker-ce/ubuntu/)



### Instruction


#### Step 1 Open Terminal: 

 ```
	docker run -d -p 5000:5000 --name xxe ti1akt/xxe:latest
```

#### Step 2 Open Browser: 

```
http://127.0.0.1:5000
```

#### To Upload a file

```
git clone https://github.com/tilakt/XXE.git
```


#### Step 3 Upload files: 

* cd into the `XXE/payloads`
* Upload a `normal_file.xml`
* press `submit`
* See the result

#### Step 4 Upload files: 

* cd into the `XXE/payloads`
* Now will try to get the passwd file information
* Upload a `payload_passwd.xml`
* press `submit`
* See the result

#### Step 5 Upload files: 

* cd into the `XXE/payloads`
* Now will try to get the shadow file information
* Upload a `payload_shadow.xml`
* press `submit`
* See the result

#### Step 6 Clean the docker

```
docker stop xxe
docker rm xxe
```

