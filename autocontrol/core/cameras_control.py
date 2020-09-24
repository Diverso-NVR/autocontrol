import logging

import timeout_decorator
import zeep
import onvif
from onvif import ONVIFCamera

zeep.xsd.simple.AnySimpleType.pythonvalue = lambda self, xmlvalue: xmlvalue


@timeout_decorator.timeout(5)
def goto_nvr_preset(ip: str, port: str) -> None:

    camera = ONVIFCamera(ip, port, "admin", "Supervisor")

    media = camera.create_media_service()
    ptz = camera.create_ptz_service()

    profile1_token = media.GetProfiles()[0].token

    requestg = ptz.create_type('GotoPreset')
    requestg.ProfileToken = profile1_token
    requestg.PresetToken = '42'

    ptz.GotoPreset(requestg)
