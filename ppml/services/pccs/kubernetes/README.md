# Deploy BigDL-PCCS on Kubernetes with Helm Charts

## Prerequests

- Please make sure you have a workable **Kubernetes cluster/machine**.
- Please make sure you have a usable https proxy.
- Please make sure you have already installed **[helm](https://helm.sh/)**.
- Please make sure you have an usable PCCS ApiKey for your platform. The PCCS uses this API key to request collaterals from Intel's Provisioning Certificate Service. User needs to subscribe first to obtain an API key. For how to subscribe to Intel Provisioning Certificate Service and receive an API key, goto https://api.portal.trustedservices.intel.com/provisioning-certification and click on 'Subscribe'.

## 1. Start BigDL-PCCS on Kubernetes 
Please make sure current workdir is `kubernetes`.

Then modify parameters in `values.yaml` as following:
```shell
# reset of other parameters in values.yaml is optional, please check according to your environment
pccsIP: your_pccs_ip_to_use_as                    --->   <an_used_ip_address_in_your_subnetwork_to_assign_to_pccs>

# Replace the below parameters according to your environment
apiKey: your_intel_pcs_server_subscription_key_obtained_through_web_registeration
countryName: your_country_name
cityName: your_city_name
organizaitonName: your_organizaition_name
commonName: server_fqdn_or_your_name
emailAddress: your_email_address
serverPassword: your_server_password_to_use 
```
Then, deploy BigDL-PCCS on kubernetes:

```bash
kubectl create namespace bigdl-pccs
helm install pccs . # pccs can be modified to any name as you like
```
Check the service whether it has successfully been running (it may take seconds):

```bash
kubectl get all -n bigdl-pccs

# you will get similar to below
NAME            READY   STATUS        RESTARTS   AGE
pod/pccs-0      1/1     Running       0          18s

NAME           TYPE        CLUSTER-IP      EXTERNAL-IP     PORT(S)     AGE
service/pccs   ClusterIP   1.7.4.251   1.2.3.4   18081/TCP   18s

NAME                    READY   AGE
statefulset.apps/pccs   1/1     18s

```

## 2. Check if pccs service is running and available:
Execute command to check if pccs service is available.
```bash
curl -v -k -G "https://<your_pccs_ip>:<your_pccs_port>/sgx/certification/v3/rootcacrl"

# you will get similar to below if success

* Uses proxy env variable no_proxy == '10.239.45.10:8081,10.112.231.51,10.239.45.10,172.168.0.205'
*   Trying 1.2.3.4:18081...
* TCP_NODELAY set
* Connected to 1.2.3.4 (1.2.3.4) port 18081 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: C=cn; ST=nanjing; L=nanjing; O=intel; OU=intel; CN=liyao; emailAddress=yao3.li@intel.com
*  start date: Oct 17 08:14:42 2022 GMT
*  expire date: Oct 17 08:14:42 2023 GMT
*  issuer: C=cn; ST=nanjing; L=nanjing; O=intel; OU=intel; CN=liyao; emailAddress=yao3.li@intel.com
*  SSL certificate verify result: self signed certificate (18), continuing anyway.
> GET /sgx/certification/v3/rootcacrl HTTP/1.1
> Host: 1.2.3.4:18081
> User-Agent: curl/7.68.0
> Accept: */*
>
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Request-ID: 64371451f83842079bded0b228fb7d1a
< Content-Type: application/x-pem-file; charset=utf-8
< Content-Length: 586
< ETag: W/"24a-lXdmj38gN2RweL6On8KEs2rk9To"
< Date: Tue, 18 Oct 2022 01:46:43 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
<
* Connection #0 to host 1.2.3.4 left intact
308201213081c80********************************************************************************************************************************************************************************************************************************
```



