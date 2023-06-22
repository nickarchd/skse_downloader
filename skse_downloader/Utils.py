import platform
from enum import Enum

VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_BUILD = 1


class PlatformType(Enum):
	PLATFORM_WIN32= 1,
	PLATFORM_LINUX= 2,
	PLATFORM_DARWIN= 3,


def using_platform():
	if platform.system() == "Windows":
		return PlatformType.PLATFORM_WIN32
	
	if platform.system() == "Linux":
		return PlatformType.PLATFORM_LINUX
	
	if platform.system() == "Darwin":
		return PlatformType.PLATFORM_DARWIN
	