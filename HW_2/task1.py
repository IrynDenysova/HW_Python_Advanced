from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator, model_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)


class User(BaseModel):
    name: str
    age: int = Field(..., ge=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @model_validator(mode='after')
    def validate_age_employed(self):
        if self.is_employed and ( self.age < 18 or self.age >= 65):
            raise ValueError('Age must be between 18 and 65')
        return self

def validate_user(json_input):
    user = User.model_validate_json(json_input)
    return User.model_dump_json(user)


if __name__ == '__main__':

    json_input = """{
        "name": "John Doe",
        "age": 70,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }"""
    try:
        print(validate_user(json_input))
    except ValidationError as e:
        print(e)
