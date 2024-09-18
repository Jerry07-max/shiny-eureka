# qa-test

**Kubernetes Deployment(Setting up using Minikube):**

- Install Minikube by following instructions from the official website by following the instructions: [https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download](url)
- Install Docker Desktop from the official website by following the instructions : [https://docs.docker.com/desktop/install/windows-install/](url)
- Ensure 'Docker Desktop' application is opened and running. Navigate to Settings > Kubernetes. Ensure the 'Enable Kubernetes' is checked. Click 'Apply and Restart' to apply the changes.
- Open 'cmd' or 'Windows Powershell' in Administrator mode and run the following codes:

  a) _To Start Minikube_:
  
    **minikube start --driver=docker**

  b) _To Build Docker images inside the environment_:

   **minikube docker-env** # This will configure docker environment for minikube

  c) _To check Minikube and Docker connectivity_:

  **docker ps** # This will list the running containers if it is successfully connected. 

- Ensure to upload the files directly from the [https://github.com/Vengatesh-m/qa-test](url) to the local repository or clone the repository to the local repository.
- Ensure the frontend and backend docker images are available in the 'frontend' and 'backend' folders respectively.
- Ensure the frontend and backend .yaml files are available in the 'Deployment' folder respectively.
- Open 'cmd' or 'Windows Powershell' in Administrator mode in the local repository where the .yaml files are available and run the following codes:

  a) _Verifying the nodes_:

  **kubectl get nodes** # This will display the nodes in the local kubernetes cluster.

  b) _Deploying Frontend and Backend services_:

  **kubectl apply -f backend-deployment.yaml
    kubectl apply -f frontend-deployment.yaml**

  c) _Verifying if the frontend and backend services are running_:

   **kubectl get pods
     kubectl get services**

  d) _Accessing frontend application_:

   **minikube service frontend-service** #This will automatically open the browser of the frontend application.

**Verification:**

- Verify that accessing the frontend URL displays the greeting message fetched from the backend. #The following message is displayed: "**Hello from the Backend!**"
- In case of any issues, perform the following actions to troubleshoot in the local repository:

  a) _Verify if the backend service is correctly exposing its API and that the frontend is making requests to the correct URL by running the following code in Powershell_:

  **kubectl exec -it <frontend-pod-name> -- /bin/sh
    curl http://backend-service:5000/greet**

  b) _In case of any issues accessing the frontend URL, check the logs of the frontend and backend pod files by running the following code in Powershell_:

  **kubectl logs <pod-name>** # <pod-name> is the NAME of the pod. For example: frontend-deployment-679599c646-8fz9h

**Automated Testing:**

- The automation testing is to be performed with Python. Ensure that the following libraries are installed for smooth functioning:

  a) _Installing libraries using Powershell_:

    **pip install requests**
  







