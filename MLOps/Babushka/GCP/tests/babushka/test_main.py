from babushka import models
from typer.testing import CliRunner

runner = CliRunner()

def test_download_auxiliary_data():
    result = runner.invoke(app, ["download_auxiliary_data"])
    assert result.exit_code == 0

def test_trigger_orchestrator():
    result = runner.invoke(app, ["trigger_orchestrator"])
    assert result.exit_code == 0

def test_compute_features():
    result = runner.invoke(app, ["compute_features"])
    assert result.exit_code == 0

def test_trainer():
    result = runner.invoke(app, ["trainer"])
    assert result.exit_code == 0

def test_load_artifacts():
    result = runner.invoke(app, ["load_artifacts"])
    assert result.exit_code == 0

