from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.model_type import ModelType
from ..models.task_type import TaskType
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyModelExternalImport")


@_attrs_define
class BodyModelExternalImport:
    """
    Attributes:
        name (Union[Unset, str]):
        task (Union[None, TaskType, Unset]):
        model_type (Union[ModelType, None, Unset]):
        model_name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):  Default: False.
        card_file (Union[Unset, File]):
        model_file (Union[Unset, File]):
        ckpt_state_path (Union[None, Unset, str]):
        model_state_path (Union[None, Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    task: Union[None, TaskType, Unset] = UNSET
    model_type: Union[ModelType, None, Unset] = UNSET
    model_name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = False
    card_file: Union[Unset, File] = UNSET
    model_file: Union[Unset, File] = UNSET
    ckpt_state_path: Union[None, Unset, str] = UNSET
    model_state_path: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        task: Union[None, Unset, str]
        if isinstance(self.task, Unset):
            task = UNSET
        elif isinstance(self.task, TaskType):
            task = self.task.value
        else:
            task = self.task

        model_type: Union[None, Unset, str]
        if isinstance(self.model_type, Unset):
            model_type = UNSET
        elif isinstance(self.model_type, ModelType):
            model_type = self.model_type.value
        else:
            model_type = self.model_type

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_public = self.is_public

        card_file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.card_file, Unset):
            card_file = self.card_file.to_tuple()

        model_file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.model_file, Unset):
            model_file = self.model_file.to_tuple()

        ckpt_state_path: Union[None, Unset, str]
        if isinstance(self.ckpt_state_path, Unset):
            ckpt_state_path = UNSET
        else:
            ckpt_state_path = self.ckpt_state_path

        model_state_path: Union[None, Unset, str]
        if isinstance(self.model_state_path, Unset):
            model_state_path = UNSET
        else:
            model_state_path = self.model_state_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if task is not UNSET:
            field_dict["task"] = task
        if model_type is not UNSET:
            field_dict["model_type"] = model_type
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if card_file is not UNSET:
            field_dict["card_file"] = card_file
        if model_file is not UNSET:
            field_dict["model_file"] = model_file
        if ckpt_state_path is not UNSET:
            field_dict["ckpt_state_path"] = ckpt_state_path
        if model_state_path is not UNSET:
            field_dict["model_state_path"] = model_state_path

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.task, Unset):
            if isinstance(self.task, TaskType):
                files.append(("task", (None, str(self.task.value).encode(), "text/plain")))
            else:
                files.append(("task", (None, str(self.task).encode(), "text/plain")))

        if not isinstance(self.model_type, Unset):
            if isinstance(self.model_type, ModelType):
                files.append(("model_type", (None, str(self.model_type.value).encode(), "text/plain")))
            else:
                files.append(("model_type", (None, str(self.model_type).encode(), "text/plain")))

        if not isinstance(self.model_name, Unset):
            if isinstance(self.model_name, str):
                files.append(("model_name", (None, str(self.model_name).encode(), "text/plain")))
            else:
                files.append(("model_name", (None, str(self.model_name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.is_public, Unset):
            files.append(("is_public", (None, str(self.is_public).encode(), "text/plain")))

        if not isinstance(self.card_file, Unset):
            files.append(("card_file", self.card_file.to_tuple()))

        if not isinstance(self.model_file, Unset):
            files.append(("model_file", self.model_file.to_tuple()))

        if not isinstance(self.ckpt_state_path, Unset):
            if isinstance(self.ckpt_state_path, str):
                files.append(("ckpt_state_path", (None, str(self.ckpt_state_path).encode(), "text/plain")))
            else:
                files.append(("ckpt_state_path", (None, str(self.ckpt_state_path).encode(), "text/plain")))

        if not isinstance(self.model_state_path, Unset):
            if isinstance(self.model_state_path, str):
                files.append(("model_state_path", (None, str(self.model_state_path).encode(), "text/plain")))
            else:
                files.append(("model_state_path", (None, str(self.model_state_path).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_task(data: object) -> Union[None, TaskType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_type_0 = TaskType(data)

                return task_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, TaskType, Unset], data)

        task = _parse_task(d.pop("task", UNSET))

        def _parse_model_type(data: object) -> Union[ModelType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_type_0 = ModelType(data)

                return model_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ModelType, None, Unset], data)

        model_type = _parse_model_type(d.pop("model_type", UNSET))

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("model_name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        is_public = d.pop("is_public", UNSET)

        _card_file = d.pop("card_file", UNSET)
        card_file: Union[Unset, File]
        if isinstance(_card_file, Unset):
            card_file = UNSET
        else:
            card_file = File(payload=BytesIO(_card_file))

        _model_file = d.pop("model_file", UNSET)
        model_file: Union[Unset, File]
        if isinstance(_model_file, Unset):
            model_file = UNSET
        else:
            model_file = File(payload=BytesIO(_model_file))

        def _parse_ckpt_state_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ckpt_state_path = _parse_ckpt_state_path(d.pop("ckpt_state_path", UNSET))

        def _parse_model_state_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_state_path = _parse_model_state_path(d.pop("model_state_path", UNSET))

        body_model_external_import = cls(
            name=name,
            task=task,
            model_type=model_type,
            model_name=model_name,
            description=description,
            is_public=is_public,
            card_file=card_file,
            model_file=model_file,
            ckpt_state_path=ckpt_state_path,
            model_state_path=model_state_path,
        )

        body_model_external_import.additional_properties = d
        return body_model_external_import

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
