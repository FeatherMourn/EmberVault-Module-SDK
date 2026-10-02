from src import module


def test_module_descriptor_is_plan_only():
    assert module.describe()["capability_state"] == "plan-only"
