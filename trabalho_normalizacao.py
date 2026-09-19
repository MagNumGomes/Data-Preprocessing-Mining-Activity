from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


PASTA = Path(__file__).parent
CSV_PATH = PASTA / "dados_maquinas.csv"


def criar_csv_ficticio(caminho: Path) -> None:
    """Cria um conjunto reproduzivel com ausencias e situacoes anormais conhecidas."""
    dados = []
    for numero in range(1, 61):
        turno = ["manha", "tarde", "noite"][numero % 3]
        dados.append(
            {
                "id_leitura": numero,
                "data": f"2026-09-{(numero % 28) + 1:02d}",
                "turno": turno,
                "temperatura_c": 65 + (numero % 8) + (4 if turno == "tarde" else 0),
                "vibracao_mm_s": round(2.0 + (numero % 6) * 0.25, 2),
                "consumo_kwh": 80 + (numero % 10) * 3,
                "horas_operacao": 6 + (numero % 5),
                "falha": "nao",
            }
        )

    quadro = pd.DataFrame(dados)

    # Anomalias conhecidas para facilitar a interpretacao do resultado.
    quadro.loc[7, "temperatura_c"] = 115
    quadro.loc[18, "vibracao_mm_s"] = 9.5
    quadro.loc[31, "consumo_kwh"] = 180
    quadro.loc[44, ["temperatura_c", "vibracao_mm_s"]] = [95, 8.0]
    quadro.loc[44, "falha"] = "sim"

    # Valores ausentes intencionais, conforme o enunciado.
    quadro.loc[12, "temperatura_c"] = None
    quadro.loc[26, "consumo_kwh"] = None
    quadro.to_csv(caminho, index=False)


def main() -> None:
    criar_csv_ficticio(CSV_PATH)
    dados = pd.read_csv(CSV_PATH, parse_dates=["data"])

    print("Dimensoes:", dados.shape)
    print("Tipos:\n", dados.dtypes)
    print("Valores ausentes:\n", dados.isna().sum())
    print(
        "Estatisticas:\n",
        dados.select_dtypes(include="number").describe().round(2),
    )

    colunas_numericas = [
        "temperatura_c",
        "vibracao_mm_s",
        "consumo_kwh",
        "horas_operacao",
    ]
    dados[colunas_numericas] = dados[colunas_numericas].fillna(
        dados[colunas_numericas].median()
    )

    dados["energia_por_hora"] = dados["consumo_kwh"] / dados["horas_operacao"]
    dados["indice_estresse"] = (
        dados["temperatura_c"] / 100
        + dados["vibracao_mm_s"] / 10
        + dados["energia_por_hora"] / 30
    )

    escaladores = {
        "minmax": MinMaxScaler(),
        "padronizado": StandardScaler(),
        "robusto": RobustScaler(),
    }
    dados_escalados = {}
    for nome, escalador in escaladores.items():
        dados_escalados[nome] = pd.DataFrame(
            escalador.fit_transform(dados[colunas_numericas]),
            columns=colunas_numericas,
        )
        print(f"\nResumo apos {nome}:")
        print(dados_escalados[nome].describe().loc[["mean", "std", "min", "max"]].round(2))

    fig, eixos = plt.subplots(1, 2, figsize=(13, 5))
    dados[colunas_numericas].boxplot(ax=eixos[0])
    eixos[0].set_title("Antes do escalonamento")
    eixos[0].tick_params(axis="x", rotation=35)
    dados_escalados["padronizado"].boxplot(ax=eixos[1])
    eixos[1].set_title("Depois da padronizacao")
    eixos[1].tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(PASTA / "comparacao_escalas.png", dpi=150)

    plt.figure(figsize=(8, 5))
    plt.scatter(
        dados["temperatura_c"],
        dados["vibracao_mm_s"],
        c=dados["indice_estresse"],
        cmap="viridis",
        s=55,
    )
    plt.xlabel("Temperatura (C)")
    plt.ylabel("Vibracao (mm/s)")
    plt.title("Temperatura x vibracao com indice de estresse")
    plt.colorbar(label="Indice de estresse")
    plt.tight_layout()
    plt.savefig(PASTA / "temperatura_vibracao.png", dpi=150)

    dados.to_csv(PASTA / "dados_maquinas_tratados.csv", index=False)
    print("\nArquivos criados:")
    print("-", CSV_PATH.name)
    print("- dados_maquinas_tratados.csv")
    print("- comparacao_escalas.png")
    print("- temperatura_vibracao.png")


if __name__ == "__main__":
    main()
