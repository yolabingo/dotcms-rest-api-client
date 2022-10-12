from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.delete_8_json_body_additional_property import Delete8JsonBodyAdditionalProperty

T = TypeVar("T", bound="Delete8JsonBody")


@attr.s(auto_attribs=True)
class Delete8JsonBody:
    """ """

    additional_properties: Dict[str, Delete8JsonBodyAdditionalProperty] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delete_8_json_body = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Delete8JsonBodyAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        delete_8_json_body.additional_properties = additional_properties
        return delete_8_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Delete8JsonBodyAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Delete8JsonBodyAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
