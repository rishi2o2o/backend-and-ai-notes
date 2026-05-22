# Helm and Kubernetes Package Management

Helm is the de facto package manager for Kubernetes that automates the creation, installation, and configuration of Kubernetes applications. It functions similarly to how apt or yum manage packages for Linux or how npm works for Node.js.


## Key Concepts of Helm

Helm uses three core concepts to manage Kubernetes applications:

1. Charts: Bundled packages containing all the YAML resource definitions (deployments, services, config maps) needed to run an application.

2. Repositories: Locations (like an app store) where Helm charts are stored and shared with others.

3. Releases: A specific instance of a chart running in a Kubernetes cluster; you can have multiple releases of the same chart (e.g., "dev-database" and "prod-database").


## Why Use Kubernetes Package Management?

Managing Kubernetes manually requires writing hundreds of static YAML files. Helm solves this by:

* Templating: Allows you to use variables (via values.yaml) to reuse the same chart across different environments like development and production.

* Versioning: Tracks changes and allows you to roll back to a previous version of an application if an update fails.

* Dependency Management: Automatically handles and installs other services your application needs to function.

* Simplification: Deploys complex applications with a single command (helm install) instead of dozens of kubectl apply commands.


## Helm vs Standard Kubernetes (kubectl)

| Feature   | kubectl                               | Helm                                 |
| --------- | ------------------------------------- | ------------------------------------ |
| Focus     | Individual resources (Pods, Services) | Entire applications (Charts)         |
| Logic     | Static YAML files                     | Dynamic templates with variables     |
| Updates   | Manual changes to files               | Automated upgrades and rollbacks     |
| Discovery | Must find/write own manifests         | Searchable Artifact Hub repositories |


## Getting Started

To use Helm, you typically follow these steps using the Helm CLI:

1. Find a chart: Search for pre-made applications on Artifact Hub or in your own repo.

2. Customize: Edit a values.yaml file to set your specific configuration (e.g., database password, number of replicas).

3. Install: Run helm install [release-name] [chart-name] to deploy the entire stack to your cluster.

4. Manage: Use helm list to see what's running or helm upgrade to apply changes.


# A Demo of Helm

## Step 1: Prepare Your Cluster

Before using Helm, you need a Kubernetes cluster running on your Mac.

1. Install kubectl to interact with Kubernetes clusters

    ```bash
    brew install kubectl
    ```

2. Start a Linux VM with 4 CPUs and 8GB RAM, featuring a built-in Kubernetes cluster and Rosetta support for running Intel-based containers on Apple Silicon

    ```bash
    colima start --kubernetes --vm-type=vz --vz-rosetta --cpu 4 --memory 8
    ```

3. Verify that the cluster is running and check the status of the node inside the VM

    ```bash
    kubectl cluster-info  

    kubectl get nodes
    ```

4. Install helm to install and manage applications on Kubernetes clusters

    ```bash
    brew install helm
    ```


## Step 2: Deploy Your First App (Nginx)

We will use Helm to install a pre-made **Chart** for an Nginx web server.

1. Add a Repository: Helm doesn't know where to look for charts until you add a **repo** (like an app store source). We'll use the Bitnami repo, which is very popular.

    ```bash
    helm repo add bitnami https://charts.bitnami.com/bitnami  

    helm repo update
    ```

2. Install the Chart: Now, let's create a **Release** called my-web-server.

    ```bash
    helm search repo nginx  

    helm install my-web-server bitnami/nginx
    ```

    Helm just generated dozens of lines of Kubernetes YAML (Deployments, Services, etc.) and sent them to your cluster in one go.


## Step 3: See Helm in Action

Now that it’s running, let's use Helm to manage it.

1. List Your Releases: Check what apps Helm is currently managing.

    ```bash
    helm list
    ```

2. Upgrade the App (The Power of Helm): Imagine you want to change the number of web server copies (replicas) from 1 to 3. Instead of editing complex YAML, you just pass a new value.

    ```bash
    helm upgrade my-web-server bitnami/nginx --set replicaCount=3
    ```

3. Check the Status: See the resources Helm created for you.

    ```bash
    kubectl get pods
    ```

    You should see 3 Nginx pods starting up because of your upgrade!


## Step 4: Cleanup

One of the best parts of Helm is how easily it cleans up every single resource it created.

1. Uninstall the Release: This removes all Kubernetes resources that Helm created for the my-web-server release.

    ```bash
    helm uninstall my-web-server
    ```




