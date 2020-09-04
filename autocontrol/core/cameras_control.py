import logging

import zeep
from onvif import ONVIFCamera

logger = logging.getLogger('autocontrol_logger')


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


def goto_home_position(ip: str, port: str) -> None:
    logger.info(f'Calling default preset on device {ip}:{port}')

    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

    camera = ONVIFCamera(ip, port, "admin", "Supervisor")

    media = camera.create_media_service()
    ptz = camera.create_ptz_service()

    profile1_token = media.GetProfiles()[0].token

    ptz.GotoHomePosition(profile1_token)
