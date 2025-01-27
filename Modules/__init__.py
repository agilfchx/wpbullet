from .SQLInjection import SQLInjection
from .CrossSiteScripting import CrossSiteScripting
from .CommandExecution import CommandExecution
from .FileDeletion import FileDeletion
from .FileInclusion import FileInclusion
from .InsecureEmail import InsecureEmail
from .XPATHInjection import XPATHInjection
from .LDAPInjection import LDAPInjection
from .HeaderInjection import HeaderInjection
from .OptionsUpdate import OptionsUpdate
from .ArbitraryFileUpload import ArbitraryFileUpload

classes = {
    'CommandExecution': CommandExecution,
    'CrossSiteScripting': CrossSiteScripting,
    'FileDeletion': FileDeletion,
    'FileInclusion': FileInclusion,
    'HeaderInjection': HeaderInjection,
    'InsecureEmail': InsecureEmail,
    'LDAPInjection': LDAPInjection,
    'OptionsUpdate': OptionsUpdate,
    'SQLInjection': SQLInjection,
    'XPATHInjection': XPATHInjection,
    'ArbitraryFileUpload': ArbitraryFileUpload
}
