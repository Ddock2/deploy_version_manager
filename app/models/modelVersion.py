from pydantic import BaseModel

class version:
    version_id: int
    major: int
    minor: int
    maintenance: int
    patch: int

    def __init__(self, version_id, major, minor, maintenance, patch):
        self.version_id = version_id
        self.major = major
        self.minor = minor
        self.maintenance = maintenance
        self.patch = patch

    def print_json(self):
        return ('{ "version_id" : "' + str(self.version_id)
                + '", "major" : "' + str(self.major)
                + '", "minor" : "' +  str(self.minor)
                + '", "maintenance" : "' + str(self.maintenance)
                + '", "patch" : "' + str(self.patch)
                + '" }')


class paramVersion(BaseModel, version):
    def __init__():
        print()
