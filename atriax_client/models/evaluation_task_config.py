from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_load_info import DatasetLoadInfo
    from ..models.model_load_info import ModelLoadInfo


T = TypeVar("T", bound="EvaluationTaskConfig")


@_attrs_define
class EvaluationTaskConfig:
    """
    Attributes:
        dataset (DatasetLoadInfo): A model representing dataset information.

            Attributes:
                id (uuid.UUID): The unique identifier of the dataset.
                branch (str): The branch of the dataset.
                split (DatasetSplitType): The split of the dataset.
        model (ModelLoadInfo): A model representing information required to load a model.

            Attributes:
                id (str): The name of the model.
                branch (str): The branch of the model.
                override_config (dict | None): Optional configuration to override the default model configuration.
    """

    dataset: "DatasetLoadInfo"
    model: "ModelLoadInfo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset = self.dataset.to_dict()

        model = self.model.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
                "model": model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_load_info import DatasetLoadInfo
        from ..models.model_load_info import ModelLoadInfo

        d = dict(src_dict)
        dataset = DatasetLoadInfo.from_dict(d.pop("dataset"))

        model = ModelLoadInfo.from_dict(d.pop("model"))

        evaluation_task_config = cls(
            dataset=dataset,
            model=model,
        )

        evaluation_task_config.additional_properties = d
        return evaluation_task_config

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
