# Python based web application to test in AKS

Procedure for AKS @ Kodekloud

1. Store sample app in github: https://github.com/look1976/linuxapp
2. Clone app locally: git clone https://github.com/look1976/linuxapp
3. Build the container with docker: docker build -t linuxapp linuxapp
4. Push container to docker.com: docker push look1976/linuxapp:v1
5. Get AKS cluster creds to local .kube/config: az aks get-Credentials --name NAMEOFYOURCLUSTER --group NAMEOFYOURRG
6. Check proper AKS cluster context: kubectl config current-context
7. Check nodes: kubectl get nodes
8. reate deployment: kubectl create deployment DEPLOYMENTNAME --image=look1976/linuxapp:v1 --replicas=1
9. Check depl: kubectl get deployment
10. Create SVC using LB: kubectl expose deployment kodekloudapp --type=LoadBalancer --port=80 --target-port=80
11 .Get public IP: kubectl get service
