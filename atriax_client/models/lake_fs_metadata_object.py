from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lake_fs_branch_summary import LakeFSBranchSummary


T = TypeVar("T", bound="LakeFSMetadataObject")


@_attrs_define
class LakeFSMetadataObject:
    """
    Attributes:
        main_branch (str):
        branches (list['LakeFSBranchSummary']):
    """

    main_branch: str
    branches: list["LakeFSBranchSummary"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_branch = self.main_branch

        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "main_branch": main_branch,
                "branches": branches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lake_fs_branch_summary import LakeFSBranchSummary

        d = dict(src_dict)
        main_branch = d.pop("main_branch")

        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = LakeFSBranchSummary.from_dict(branches_item_data)

            branches.append(branches_item)

        lake_fs_metadata_object = cls(
            main_branch=main_branch,
            branches=branches,
        )

        lake_fs_metadata_object.additional_properties = d
        return lake_fs_metadata_object

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
