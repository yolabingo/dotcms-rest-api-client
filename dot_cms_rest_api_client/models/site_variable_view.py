import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteVariableView")


@attr.s(auto_attribs=True)
class SiteVariableView:
    """
    Attributes:
        id (Union[Unset, str]):
        host_id (Union[Unset, str]):
        name (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        last_modifier_id (Union[Unset, str]):
        last_mod_date (Union[Unset, datetime.datetime]):
        last_modifier_full_name (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    host_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    last_modifier_id: Union[Unset, str] = UNSET
    last_mod_date: Union[Unset, datetime.datetime] = UNSET
    last_modifier_full_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        host_id = self.host_id
        name = self.name
        key = self.key
        value = self.value
        last_modifier_id = self.last_modifier_id
        last_mod_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_mod_date, Unset):
            last_mod_date = self.last_mod_date.isoformat()

        last_modifier_full_name = self.last_modifier_full_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if last_modifier_id is not UNSET:
            field_dict["lastModifierId"] = last_modifier_id
        if last_mod_date is not UNSET:
            field_dict["lastModDate"] = last_mod_date
        if last_modifier_full_name is not UNSET:
            field_dict["lastModifierFullName"] = last_modifier_full_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        host_id = d.pop("hostId", UNSET)

        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        last_modifier_id = d.pop("lastModifierId", UNSET)

        _last_mod_date = d.pop("lastModDate", UNSET)
        last_mod_date: Union[Unset, datetime.datetime]
        if isinstance(_last_mod_date, Unset):
            last_mod_date = UNSET
        else:
            last_mod_date = isoparse(_last_mod_date)

        last_modifier_full_name = d.pop("lastModifierFullName", UNSET)

        site_variable_view = cls(
            id=id,
            host_id=host_id,
            name=name,
            key=key,
            value=value,
            last_modifier_id=last_modifier_id,
            last_mod_date=last_mod_date,
            last_modifier_full_name=last_modifier_full_name,
        )

        site_variable_view.additional_properties = d
        return site_variable_view

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
