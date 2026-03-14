import pandas as pd


def profile_dataset(df: pd.DataFrame, dataset_name: str) -> dict:
    """
    Extrai metadados automáticos de um DataFrame.
    Retorna um dicionário estruturado pronto para exportação.
    """
    total_rows, total_cols = df.shape

    columns = []
    for col in df.columns:
        col_data = df[col]
        col_info = {
            "name": col,
            "type": str(col_data.dtype),
            "null_count": int(col_data.isnull().sum()),
            "null_pct": round(col_data.isnull().mean() * 100, 2),
            "unique_count": int(col_data.nunique()),
        }

        # Estatísticas para colunas numéricas
        if pd.api.types.is_numeric_dtype(col_data):
            col_info["min"] = round(float(col_data.min()), 4)
            col_info["max"] = round(float(col_data.max()), 4)
            col_info["mean"] = round(float(col_data.mean()), 4)
        else:
            # Exemplos de valores para colunas de texto/data
            col_info["sample_values"] = [str(v) for v in col_data.dropna().unique()[:3].tolist()]

        columns.append(col_info)

    return {
        "dataset_name": dataset_name,
        "total_rows": total_rows,
        "total_columns": total_cols,
        "columns": columns,
    }
