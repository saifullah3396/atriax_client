from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LakeFSStorageObject")


@_attrs_define
class LakeFSStorageObject:
    """
    Attributes:
        object_key (str):
        ext (str):
        path (str):
        physical_address (Union[None, Unset, str]):
        presigned_url (Union[None, Unset, str]):
        size (Union[Unset, int]):  Default: 0.
        modified (Union[Unset, int]):  Default: 0.
        type_ (Union[Unset, str]):  Default: 'file'.
    """

    object_key: str
    ext: str
    path: str
    physical_address: Union[None, Unset, str] = UNSET
    presigned_url: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = 0
    modified: Union[Unset, int] = 0
    type_: Union[Unset, str] = "file"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_key = self.object_key

        ext = self.ext

        path = self.path

        physical_address: Union[None, Unset, str]
        if isinstance(self.physical_address, Unset):
            physical_address = UNSET
        else:
            physical_address = self.physical_address

        presigned_url: Union[None, Unset, str]
        if isinstance(self.presigned_url, Unset):
            presigned_url = UNSET
        else:
            presigned_url = self.presigned_url

        size = self.size

        modified = self.modified

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_key": object_key,
                "ext": ext,
                "path": path,
            }
        )
        if physical_address is not UNSET:
            field_dict["physical_address"] = physical_address
        if presigned_url is not UNSET:
            field_dict["presigned_url"] = presigned_url
        if size is not UNSET:
            field_dict["size"] = size
        if modified is not UNSET:
            field_dict["modified"] = modified
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_key = d.pop("object_key")

        ext = d.pop("ext")

        path = d.pop("path")

        def _parse_physical_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        physical_address = _parse_physical_address(d.pop("physical_address", UNSET))

        def _parse_presigned_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        presigned_url = _parse_presigned_url(d.pop("presigned_url", UNSET))

        size = d.pop("size", UNSET)

        modified = d.pop("modified", UNSET)

        type_ = d.pop("type", UNSET)

        lake_fs_storage_object = cls(
            object_key=object_key,
            ext=ext,
            path=path,
            physical_address=physical_address,
            presigned_url=presigned_url,
            size=size,
            modified=modified,
            type_=type_,
        )

        lake_fs_storage_object.additional_properties = d
        return lake_fs_storage_object

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
