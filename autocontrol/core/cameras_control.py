import logging

import timeout_decorator
import zeep
from onvif import ONVIFCamera

logger = logging.getLogger('autocontrol_logger')


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


@timeout_decorator.timeout(5)
def goto_home_position(ip: str, port: str) -> None:
    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

    camera = ONVIFCamera(ip, port, "admin", "Supervisor")

    media = camera.create_media_service()
    ptz = camera.create_ptz_service()

    profile1_token = media.GetProfiles()[0].token

    ptz.GotoHomePosition(profile1_token)
