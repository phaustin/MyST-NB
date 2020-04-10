import pytest


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "cache"}
)
def test_basic_unrun(sphinx_run, file_regression, check_nbs):
    """The outputs should be populated."""
    sphinx_run.build()
    assert sphinx_run.warnings() == ""
    assert "test_name" in sphinx_run.app.env.metadata["basic_unrun"]
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "cache"}
)
def test_rebuild_cache(sphinx_run):
    """The notebook should only be executed once."""
    sphinx_run.build()
    assert "Executing" in sphinx_run.status(), sphinx_run.status()
    sphinx_run.invalidate_files()
    sphinx_run.build()
    assert "Executing" not in sphinx_run.status(), sphinx_run.status()


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "force"}
)
def test_rebuild_force(sphinx_run):
    """The notebook should be executed twice."""
    sphinx_run.build()
    assert "Executing" in sphinx_run.status(), sphinx_run.status()
    sphinx_run.invalidate_files()
    sphinx_run.build()
    assert "Executing" in sphinx_run.status(), sphinx_run.status()


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb",
    conf={
        "jupyter_execute_notebooks": "cache",
        "execution_excludepatterns": ["basic_*"],
    },
)
def test_exclude_path(sphinx_run, file_regression):
    """The notebook should not be executed."""
    sphinx_run.build()
    assert len(sphinx_run.app.env.excluded_nb_exec_paths) == 1
    assert "Executing" not in sphinx_run.status(), sphinx_run.status()
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "basic_failing.ipynb", conf={"jupyter_execute_notebooks": "cache"}
)
def test_basic_failing(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert "Execution Failed" in sphinx_run.warnings()
    assert (
        "Couldn't find cache key for notebook file source/basic_failing.ipynb"
        in sphinx_run.warnings()
    )
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")
    sphinx_run.get_report_file()


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "auto"}
)
def test_basic_unrun_nbclient(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    assert "test_name" in sphinx_run.app.env.metadata["basic_unrun"]
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "force"}
)
def test_outputs_present(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    assert "test_name" in sphinx_run.app.env.metadata["basic_unrun"]
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "complex_outputs_unrun.ipynb", conf={"jupyter_execute_notebooks": "cache"}
)
def test_complex_outputs_unrun(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "complex_outputs_unrun.ipynb", conf={"jupyter_execute_notebooks": "auto"}
)
def test_complex_outputs_unrun_nbclient(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "off"}
)
def test_no_execute(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    # print(sphinx_run.status())
    assert sphinx_run.warnings() == ""
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")


@pytest.mark.sphinx_params(
    "basic_unrun.ipynb", conf={"jupyter_execute_notebooks": "cache"}
)
def test_jupyter_cache_path(sphinx_run, file_regression, check_nbs):
    sphinx_run.build()
    assert "Execution Succeeded" in sphinx_run.status()
    assert sphinx_run.warnings() == ""
    file_regression.check(sphinx_run.get_nb(), check_fn=check_nbs, extension=".ipynb")
    file_regression.check(sphinx_run.get_doctree().pformat(), extension=".xml")
