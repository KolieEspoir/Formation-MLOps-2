from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"


def test_to_csv_called_with_index_false():
    for file_path in PACKAGE_ROOT.rglob("*.py"):
        content = file_path.read_text()

        nb_to_csv = content.count(".to_csv(")
        nb_index_false = content.count("index=False")

        assert nb_to_csv == nb_index_false, (
            f"{file_path}: tous les appels à to_csv doivent utiliser index=False"
        )
