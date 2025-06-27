from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_instance_type import DataInstanceType
from ..models.dataset_status import DatasetStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lake_fs_metadata_object import LakeFSMetadataObject


T = TypeVar("T", bound="DatasetListItem")


@_attrs_define
class DatasetListItem:
    """
    Attributes:
        id (UUID):
        created_at (str):
        updated_at (str):
        name (str):
        data_instance_type (DataInstanceType):
        user_id (UUID):
        storage_metadata (LakeFSMetadataObject):
        description (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):  Default: False.
        status (Union[Unset, DatasetStatus]):
    """

    id: UUID
    created_at: str
    updated_at: str
    name: str
    data_instance_type: DataInstanceType
    user_id: UUID
    storage_metadata: "LakeFSMetadataObject"
    description: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = False
    status: Union[Unset, DatasetStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        data_instance_type = self.data_instance_type.value

        user_id = str(self.user_id)

        storage_metadata = self.storage_metadata.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_public = self.is_public

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "data_instance_type": data_instance_type,
                "user_id": user_id,
                "storage_metadata": storage_metadata,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lake_fs_metadata_object import LakeFSMetadataObject

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        name = d.pop("name")

        data_instance_type = DataInstanceType(d.pop("data_instance_type"))

        user_id = UUID(d.pop("user_id"))

        storage_metadata = LakeFSMetadataObject.from_dict(d.pop("storage_metadata"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        is_public = d.pop("is_public", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DatasetStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatasetStatus(_status)

        dataset_list_item = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            data_instance_type=data_instance_type,
            user_id=user_id,
            storage_metadata=storage_metadata,
            description=description,
            is_public=is_public,
            status=status,
        )

        dataset_list_item.additional_properties = d
        return dataset_list_item

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
