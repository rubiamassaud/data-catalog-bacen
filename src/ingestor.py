import pandas as pd
import requests
from datetime import datetime, timedelta

SERIES = {
    "selic":    11,
    "ipca":    433,
    "cambio":    1,
    "igpm":    189,
    "pib":    4380,
}

def load_bacen_series(codigo: int, nome: str, dias: int = 365) -> pd.DataFrame:
    """
    Busca uma série temporal do Banco Central via API pública.
    """
    data_fim = datetime.today().strftime("%d/%m/%Y")
    data_ini = (datetime.today() - timedelta(days=dias)).strftime("%d/%m/%Y")

    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}"
        f"/dados?formato=json&dataInicial={data_ini}&dataFinal={data_fim}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    df = pd.DataFrame(response.json())
    df.columns = ["data", "valor"]
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)
    df["serie"] = nome

    print(f"[ingestor] {nome.upper()}: {len(df)} registros carregados")
    return df


def load_dataset(series: dict = SERIES, dias: int = 365) -> pd.DataFrame:
    """
    Carrega múltiplas séries do BACEN e consolida em um único DataFrame.
    """
    frames = []
    for nome, codigo in series.items():
        try:
            df = load_bacen_series(codigo, nome, dias)
            frames.append(df)
        except Exception as e:
            print(f"[ingestor] Erro ao carregar {nome}: {e}")

    return pd.concat(frames, ignore_index=True)
