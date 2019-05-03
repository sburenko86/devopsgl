1. Clone project from GitHub repo:  
git clone ...

2. Add privilege to execute files:  
chmod +x DevOps/*

3. Create image:  
user@user:~/DevOpsGL$ docker build -t metrics .

4. Checking image (Optional):  
user@user:~/DevOpsGL$ docker image ls

5. Create and run container:  
field = [mem, cpu] # choose only one  
user@user:~/DevOpsGL$ docker run metrics ./metrics.py $filed

6. Checking container (Optional):   
user@user:~/DevOpsGL$ docker ps -a
