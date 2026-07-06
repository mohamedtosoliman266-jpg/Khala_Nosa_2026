from app.skills.calculator import CalculatorSkill


def run():

    skill = CalculatorSkill()

    assert skill.can_handle("2+2")
    assert skill.can_handle("25*18")
    assert not skill.can_handle("السلام عليكم")

    assert skill.handle("2+2") == "الناتج = 4"
    assert skill.handle("25*18") == "الناتج = 450"

    print("✅ Calculator Tests Passed")


if __name__ == "__main__":
    run()
