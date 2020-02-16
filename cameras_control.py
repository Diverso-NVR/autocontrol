import re

from onvif import ONVIFCamera


def call_default_preset(onvif_ip: str) -> None:
    user, password, host, port = re.split("[@:]", onvif_ip)

    onvif_camera = ONVIFCamera(host, port, user, password, '/etc/onvif/wsdl/')
    ptz = onvif_camera.create_ptz_service()

    pass
