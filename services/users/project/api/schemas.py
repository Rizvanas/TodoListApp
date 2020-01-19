from project import ma
from project.api.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        dump_only = ("id", "active")
