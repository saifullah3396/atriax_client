from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_load_info_override_config_type_0 import ModelLoadInfoOverrideConfigType0


T = TypeVar("T", bound="ModelLoadInfo")


@_attrs_define
class ModelLoadInfo:
    """A model representing information required to load a model.

    Attributes:
        id (str): The name of the model.
        branch (str): The branch of the model.
        override_config (dict | None): Optional configuration to override the default model configuration.

        Attributes:
            id (UUID):
            name (Union[None, Unset, str]):
            config_name (Union[Unset, str]):  Default: 'default'.
            branch (Union[Unset, str]):  Default: 'main'.
            override_config (Union['ModelLoadInfoOverrideConfigType0', None, Unset]):
    """

    id: UUID
    name: Union[None, Unset, str] = UNSET
    config_name: Union[Unset, str] = "default"
    branch: Union[Unset, str] = "main"
    override_config: Union["ModelLoadInfoOverrideConfigType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_load_info_override_config_type_0 import ModelLoadInfoOverrideConfigType0

        id = str(self.id)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config_name = self.config_name

        branch = self.branch

        override_config: Union[None, Unset, dict[str, Any]]
        if isinstance(self.override_config, Unset):
            override_config = UNSET
        elif isinstance(self.override_config, ModelLoadInfoOverrideConfigType0):
            override_config = self.override_config.to_dict()
        else:
            override_config = self.override_config

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
        if override_config is not UNSET:
            field_dict["override_config"] = override_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_load_info_override_config_type_0 import ModelLoadInfoOverrideConfigType0

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

        def _parse_override_config(data: object) -> Union["ModelLoadInfoOverrideConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                override_config_type_0 = ModelLoadInfoOverrideConfigType0.from_dict(data)

                return override_config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelLoadInfoOverrideConfigType0", None, Unset], data)

        override_config = _parse_override_config(d.pop("override_config", UNSET))

        model_load_info = cls(
            id=id,
            name=name,
            config_name=config_name,
            branch=branch,
            override_config=override_config,
        )

        model_load_info.additional_properties = d
        return model_load_info

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
