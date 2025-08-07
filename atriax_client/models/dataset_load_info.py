from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_split_type import DatasetSplitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetLoadInfo")


@_attrs_define
class DatasetLoadInfo:
    """A model representing dataset information.

    Attributes:
        id (uuid.UUID): The unique identifier of the dataset.
        branch (str): The branch of the dataset.
        split (DatasetSplitType): The split of the dataset.

        Attributes:
            id (UUID):
            name (Union[None, Unset, str]):
            config_name (Union[Unset, str]):  Default: 'default'.
            branch (Union[Unset, str]):  Default: 'main'.
            split (Union[Unset, DatasetSplitType]): An enumeration representing the dataset splits.

                Attributes:
                    train (str): Represents the training split of the dataset.
                    test (str): Represents the testing split of the dataset.
                    validation (str): Represents the validation split of the dataset.
            sample_indices (Union[None, Unset, list[int]]):
    """

    id: UUID
    name: Union[None, Unset, str] = UNSET
    config_name: Union[Unset, str] = "default"
    branch: Union[Unset, str] = "main"
    split: Union[Unset, DatasetSplitType] = UNSET
    sample_indices: Union[None, Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config_name = self.config_name

        branch = self.branch

        split: Union[Unset, str] = UNSET
        if not isinstance(self.split, Unset):
            split = self.split.value

        sample_indices: Union[None, Unset, list[int]]
        if isinstance(self.sample_indices, Unset):
            sample_indices = UNSET
        elif isinstance(self.sample_indices, list):
            sample_indices = self.sample_indices

        else:
            sample_indices = self.sample_indices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if branch is not UNSET:
            field_dict["branch"] = branch
        if split is not UNSET:
            field_dict["split"] = split
        if sample_indices is not UNSET:
            field_dict["sample_indices"] = sample_indices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        config_name = d.pop("config_name", UNSET)

        branch = d.pop("branch", UNSET)

        _split = d.pop("split", UNSET)
        split: Union[Unset, DatasetSplitType]
        if isinstance(_split, Unset):
            split = UNSET
        else:
            split = DatasetSplitType(_split)

        def _parse_sample_indices(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sample_indices_type_0 = cast(list[int], data)

                return sample_indices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        sample_indices = _parse_sample_indices(d.pop("sample_indices", UNSET))

        dataset_load_info = cls(
            id=id,
            name=name,
            config_name=config_name,
            branch=branch,
            split=split,
            sample_indices=sample_indices,
        )

        dataset_load_info.additional_properties = d
        return dataset_load_info

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
