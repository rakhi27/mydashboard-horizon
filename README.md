# MyDashboard Horizon Extension

1. Install module

    ```
    git clone https://github.com/rakhi27/mydashboard-horizon.git
    pip install -e mydashboard-horizon
    ```

2. Copy extension files from the project root folder to ```/etc/openstack_dashboard/local/enabled``` or to ```/opt/stack/horizon/openstack_dashboard/local/enabled``` folder

    ```
    cp openstack_dashboard_extensions/*.py /opt/stack/horizon/openstack_dashboard/local/enabled/
    ```

