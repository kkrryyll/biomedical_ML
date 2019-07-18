from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from grandchallenge.core.widgets import JSONEditorWidget
from grandchallenge.reader_studies.models import (
    ReaderStudy,
    HANGING_LIST_SCHEMA,
    Question,
)


class SaveFormInitMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit("save", "Save"))


class ReaderStudyCreateForm(SaveFormInitMixin, ModelForm):
    class Meta:
        model = ReaderStudy
        fields = ("title", "description")


class ReaderStudyUpdateForm(ReaderStudyCreateForm, ModelForm):
    class Meta(ReaderStudyCreateForm.Meta):
        fields = ("title", "description", "hanging_list")
        widgets = {
            "hanging_list": JSONEditorWidget(schema=HANGING_LIST_SCHEMA)
        }


class QuestionCreateForm(SaveFormInitMixin, ModelForm):
    class Meta:
        model = Question
        fields = ("question_text", "answer_type", "order")
