# MyDashboard Horizon Extension

1. Install module

    ```
    git clone https://github.com/rakhi27/mydashboard-horizon.git
    pip install -e mydashboard-horizon
    ```

2. Copy extension files from the project root folder to ```openstack_dashboard_extensions``` or to ```/opt/stack/horizon/openstack_dashboard/enabled``` folder

    ```
    cp openstack_dashboard_extensions/*.py /opt/stack/horizon/openstack_dashboard/enabled/
    ```

3. Django has a compressor feature that performs many enhancements for the delivery of static files.so compress the js and css/scss files run the following command

	```
    python manage.py compress
    ```

4. Restart the apache2 server

    ```
    sudo service apache2 restart
    ```
