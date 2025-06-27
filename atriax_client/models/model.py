from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_type import TaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lake_fs_metadata_object import LakeFSMetadataObject


T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """
    Attributes:
        id (UUID):
        created_at (str):
        updated_at (str):
        name (str):
        description (str):
        task_type (TaskType):
        user_id (UUID):
        storage_metadata (LakeFSMetadataObject):
        is_public (Union[Unset, bool]):  Default: False.
        card_url (Union[None, Unset, str]):
    """

    id: UUID
    created_at: str
    updated_at: str
    name: str
    description: str
    task_type: TaskType
    user_id: UUID
    storage_metadata: "LakeFSMetadataObject"
    is_public: Union[Unset, bool] = False
    card_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        description = self.description

        task_type = self.task_type.value

        user_id = str(self.user_id)

        storage_metadata = self.storage_metadata.to_dict()

        is_public = self.is_public

        card_url: Union[None, Unset, str]
        if isinstance(self.card_url, Unset):
            card_url = UNSET
        else:
            card_url = self.card_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "description": description,
                "task_type": task_type,
                "user_id": user_id,
                "storage_metadata": storage_metadata,
            }
        )
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if card_url is not UNSET:
            field_dict["card_url"] = card_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lake_fs_metadata_object import LakeFSMetadataObject

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        name = d.pop("name")

        description = d.pop("description")

        task_type = TaskType(d.pop("task_type"))

        user_id = UUID(d.pop("user_id"))

        storage_metadata = LakeFSMetadataObject.from_dict(d.pop("storage_metadata"))

        is_public = d.pop("is_public", UNSET)

        def _parse_card_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        card_url = _parse_card_url(d.pop("card_url", UNSET))

        model = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            task_type=task_type,
            user_id=user_id,
            storage_metadata=storage_metadata,
            is_public=is_public,
            card_url=card_url,
        )

        model.additional_properties = d
        return model

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
