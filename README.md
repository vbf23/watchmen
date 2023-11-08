# Start Here (SSH into Compute Instance)
```bash
$ cd
$ cd ../../
$ cd var/www/html
$ sudo git clone <this URL>
```
# Install (OCI or Azure instance)
```bash
$ cd <this URL> 
$ sudo chmod +x install_oci.sh
$ ./install_oci.sh
```
# Run
```bash
$ sudo mv watch_men.py ../
$ cd ../
$ sudo python3 watch_men.py
```
# Expect to see the following
```bash
 * Serving Flask app 'watch_men' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.0.100:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
# Access your compute instance via IP address
## Open browser and place your IP address in the browser
