import json
from pathlib import Path
from datetime import datetime


def export_catalog(profile: dict, report: str, output_dir: str = "output"):
    """
    Exporta o catálogo completo em JSON e Markdown.
    """
    Path(output_dir).mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"{profile['dataset_name']}_{timestamp}"

    # --- Exporta JSON ---
    catalog = {**profile, "llm_report": report}
    json_path = f"{output_dir}/{base_name}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    # --- Exporta Markdown ---
    md_lines = [
        f"# Catálogo: {profile['dataset_name']}",
        f"\n**Gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"\n## Visão Geral\n",
        f"- **Linhas:** {profile['total_rows']}",
        f"- **Colunas:** {profile['total_columns']}",
        f"\n## Análise do LLM\n",
        report,
        f"\n## Detalhes das Colunas\n",
        "| Coluna | Tipo | Nulos (%) | Únicos |",
        "|--------|------|-----------|--------|",
    ]
    for col in profile["columns"]:
        md_lines.append(
            f"| {col['name']} | {col['type']} | {col['null_pct']}% | {col['unique_count']} |"
        )

    md_path = f"{output_dir}/{base_name}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"[exporter] Catálogo salvo em: {json_path} e {md_path}")
    return json_path, md_path
