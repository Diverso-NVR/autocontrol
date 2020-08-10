import zeep
from onvif import ONVIFCamera
import timeout_decorator


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


@timeout_decorator.timeout(3)
def goto_home_position(ip: str, port: str) -> None:
    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

    camera = ONVIFCamera(ip, port, "admin", "Supervisor")

    media = camera.create_media_service()
    ptz = camera.create_ptz_service()

    profile1_token = media.GetProfiles()[0].token

    ptz.GotoHomePosition(profile1_token)

    print(f"Successfully moved {ip} to home position")
