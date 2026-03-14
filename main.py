import argparse
from src.ingestor import load_dataset
from src.profiler import profile_dataset
from src.reporter import generate_report
from src.exporter import export_catalog


def main():
    parser = argparse.ArgumentParser(description="Data Catalog Pipeline - BACEN")
    parser.add_argument("--name", default="bacen_mercado", help="Nome do dataset")
    parser.add_argument("--dias", type=int, default=365, help="Janela histórica em dias")
    parser.add_argument("--output", default="output", help="Pasta de saída")
    args = parser.parse_args()

    print("\n=== Data Catalog Pipeline — Banco Central ===\n")

    df = load_dataset(dias=args.dias)
    profile = profile_dataset(df, args.name)
    report = generate_report(profile)
    export_catalog(profile, report, args.output)

    print("\n✓ Pipeline concluído com sucesso!")


if __name__ == "__main__":
    main()
