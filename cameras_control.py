import zeep
from onvif import ONVIFCamera


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


def call_default_preset(ip: str, port: str) -> None:
    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

    camera = ONVIFCamera(ip, port, "admin", "Supervisor")

    media = camera.create_media_service()
    ptz = camera.create_ptz_service()

    profile1 = media.GetProfiles()[0].token
    preset1 = ptz.GetPresets(profile1)[0].token

    ptz.GotoPreset(profile1, preset1)
