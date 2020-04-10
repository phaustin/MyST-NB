import pytest
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.displaypub import DisplayPublisher
from docutils.transforms import Transformer

from myst_nb.nb_glue import glue, transform, utils
from myst_nb.nb_glue.domain import NbGlueDomain
from myst_nb.transform import CellOutputsToNodes


class MockDisplayPublisher(DisplayPublisher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.publish_calls = []

    def publish(self, data, **kwargs):
        kwargs["data"] = data
        self.publish_calls.append(kwargs)


@pytest.fixture()
def mock_ipython():
    shell = InteractiveShell.instance()  # type: InteractiveShell
    shell.display_pub = MockDisplayPublisher()
    yield shell.display_pub
    InteractiveShell.clear_instance()


def test_glue_func_text(mock_ipython):
    glue("a", "b")
    assert mock_ipython.publish_calls == [
        {
            "metadata": {"scrapbook": {"name": "a", "mime_prefix": ""}},
            "data": {"text/plain": "'b'"},
        }
    ]


def test_glue_func_obj(mock_ipython):
    class Obj:
        def __repr__(self):
            return "repr"

        def _repr_html_(self):
            return "<p>repr</p>"

    glue("a", Obj())
    assert mock_ipython.publish_calls == [
        {
            "metadata": {"scrapbook": {"name": "a", "mime_prefix": ""}},
            "data": {"text/html": "<p>repr</p>", "text/plain": "repr"},
        }
    ]


def test_glue_func_obj_no_display(mock_ipython):
    class Obj:
        def __repr__(self):
            return "repr"

        def _repr_html_(self):
            return "<p>repr</p>"

    glue("a", Obj(), display=False)
    assert mock_ipython.publish_calls == [
        {
            "metadata": {
                "scrapbook": {
                    "name": "a",
                    "mime_prefix": "application/papermill.record/",
                }
            },
            "data": {
                "application/papermill.record/text/html": "<p>repr</p>",
                "application/papermill.record/text/plain": "repr",
            },
        }
    ]


def test_find_glued_key(get_test_path):

    bundle = utils.find_glued_key(get_test_path("with_glue.ipynb"), "key_text1")
    assert bundle == {"key_text1": "'text1'"}

    with pytest.raises(KeyError):
        utils.find_glued_key(get_test_path("with_glue.ipynb"), "unknown")


def test_find_all_keys(get_test_path):
    keys = utils.find_all_keys(get_test_path("with_glue.ipynb"))
    assert set(keys) == {
        "key_text1",
        "key_float",
        "key_undisplayed",
        "key_df",
        "key_plt",
        "sym_eq",
    }


@pytest.mark.sphinx_params("with_glue.ipynb", conf={"jupyter_execute_notebooks": "off"})
def test_parser(sphinx_run, file_regression):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    document = sphinx_run.get_doctree()
    transformer = Transformer(document)
    transformer.add_transforms([CellOutputsToNodes, transform.PasteNodesToDocutils])
    transformer.apply_transforms()
    file_regression.check(document.pformat(), extension=".xml")
    glue_domain = NbGlueDomain.from_env(sphinx_run.app.env)
    assert set(glue_domain.cache) == {
        "key_text1",
        "key_float",
        "key_undisplayed",
        "key_df",
        "key_plt",
        "sym_eq",
    }
    glue_domain.clear_doc("with_glue")
    assert glue_domain.cache == {}
    assert glue_domain.docmap == {}
