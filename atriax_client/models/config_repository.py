from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lake_fs_metadata_object import LakeFSMetadataObject


T = TypeVar("T", bound="ConfigRepository")


@_attrs_define
class ConfigRepository:
    """
    Attributes:
        id (UUID):
        created_at (str):
        updated_at (str):
        name (str):
        description (str):
        type_ (str):
        repo_id (str):
        user_id (UUID):
        default_branch (Union[Unset, str]):  Default: 'main'.
        is_public (Union[Unset, bool]):  Default: False.
        storage_metadata (Union['LakeFSMetadataObject', None, Unset]):
    """

    id: UUID
    created_at: str
    updated_at: str
    name: str
    description: str
    type_: str
    repo_id: str
    user_id: UUID
    default_branch: Union[Unset, str] = "main"
    is_public: Union[Unset, bool] = False
    storage_metadata: Union["LakeFSMetadataObject", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.lake_fs_metadata_object import LakeFSMetadataObject

        id = str(self.id)

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        description = self.description

        type_ = self.type_

        repo_id = self.repo_id

        user_id = str(self.user_id)

        default_branch = self.default_branch

        is_public = self.is_public

        storage_metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.storage_metadata, Unset):
            storage_metadata = UNSET
        elif isinstance(self.storage_metadata, LakeFSMetadataObject):
            storage_metadata = self.storage_metadata.to_dict()
        else:
            storage_metadata = self.storage_metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "description": description,
                "type": type_,
                "repo_id": repo_id,
                "user_id": user_id,
            }
        )
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if storage_metadata is not UNSET:
            field_dict["storage_metadata"] = storage_metadata

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

        type_ = d.pop("type")

        repo_id = d.pop("repo_id")

        user_id = UUID(d.pop("user_id"))

        default_branch = d.pop("default_branch", UNSET)

        is_public = d.pop("is_public", UNSET)

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

        config_repository = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            type_=type_,
            repo_id=repo_id,
            user_id=user_id,
            default_branch=default_branch,
            is_public=is_public,
            storage_metadata=storage_metadata,
        )

        return config_repository
