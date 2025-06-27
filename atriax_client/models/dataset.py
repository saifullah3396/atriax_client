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
    from ..models.user_task import UserTask


T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """
    Attributes:
        id (UUID):
        created_at (str):
        updated_at (str):
        name (str):
        data_instance_type (DataInstanceType):
        user_id (UUID):
        under_processing (Dataset):
        description (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):  Default: False.
        status (Union[Unset, DatasetStatus]):
        storage_metadata (Union['LakeFSMetadataObject', None, Unset]):
        card_url (Union[None, Unset, str]):
        config_url (Union[None, Unset, str]):
        tasks (Union[Unset, list['UserTask']]):
    """

    id: UUID
    created_at: str
    updated_at: str
    name: str
    data_instance_type: DataInstanceType
    user_id: UUID
    under_processing: "Dataset"
    description: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = False
    status: Union[Unset, DatasetStatus] = UNSET
    storage_metadata: Union["LakeFSMetadataObject", None, Unset] = UNSET
    card_url: Union[None, Unset, str] = UNSET
    config_url: Union[None, Unset, str] = UNSET
    tasks: Union[Unset, list["UserTask"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lake_fs_metadata_object import LakeFSMetadataObject

        id = str(self.id)

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        data_instance_type = self.data_instance_type.value

        user_id = str(self.user_id)

        under_processing = self.under_processing.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_public = self.is_public

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.storage_metadata, Unset):
            storage_metadata = UNSET
        elif isinstance(self.storage_metadata, LakeFSMetadataObject):
            storage_metadata = self.storage_metadata.to_dict()
        else:
            storage_metadata = self.storage_metadata

        card_url: Union[None, Unset, str]
        if isinstance(self.card_url, Unset):
            card_url = UNSET
        else:
            card_url = self.card_url

        config_url: Union[None, Unset, str]
        if isinstance(self.config_url, Unset):
            config_url = UNSET
        else:
            config_url = self.config_url

        tasks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

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
                "under_processing": under_processing,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if status is not UNSET:
            field_dict["status"] = status
        if storage_metadata is not UNSET:
            field_dict["storage_metadata"] = storage_metadata
        if card_url is not UNSET:
            field_dict["card_url"] = card_url
        if config_url is not UNSET:
            field_dict["config_url"] = config_url
        if tasks is not UNSET:
            field_dict["tasks"] = tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lake_fs_metadata_object import LakeFSMetadataObject
        from ..models.user_task import UserTask

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        name = d.pop("name")

        data_instance_type = DataInstanceType(d.pop("data_instance_type"))

        user_id = UUID(d.pop("user_id"))

        under_processing = Dataset.from_dict(d.pop("under_processing"))

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

        def _parse_storage_metadata(data: object) -> Union["LakeFSMetadataObject", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storage_metadata_type_0 = LakeFSMetadataObject.from_dict(data)

                return storage_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["LakeFSMetadataObject", None, Unset], data)

        storage_metadata = _parse_storage_metadata(d.pop("storage_metadata", UNSET))

        def _parse_card_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        card_url = _parse_card_url(d.pop("card_url", UNSET))

        def _parse_config_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        config_url = _parse_config_url(d.pop("config_url", UNSET))

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = UserTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        dataset = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            data_instance_type=data_instance_type,
            user_id=user_id,
            under_processing=under_processing,
            description=description,
            is_public=is_public,
            status=status,
            storage_metadata=storage_metadata,
            card_url=card_url,
            config_url=config_url,
            tasks=tasks,
        )

        dataset.additional_properties = d
        return dataset

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
