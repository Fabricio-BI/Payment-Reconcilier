import pandas as pd
import sqlalchemy as sa
import logging
import os

log = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(__file__)
DB_PATH  = os.path.join(BASE_DIR, "..", "data", "processed", "conciliador.db")
DATA_DIR = os.path.join(BASE_DIR, "..", "data", "processed")


def cargar_a_sqlite(tabla_maestra_path: str, duplicados_path: str):
    log.info("Conectando a SQLite: %s", DB_PATH)

    engine = sa.create_engine(f"sqlite:///{DB_PATH}")

    # Leer los archivos procesados
    df_main = pd.read_csv(tabla_maestra_path)
    df_dups = pd.read_csv(duplicados_path)

    # Agregar columna de período
    periodo_actual = pd.Timestamp.today().strftime("%Y-%m")
    df_main["periodo"] = periodo_actual
    df_dups["periodo"] = periodo_actual

    # Eliminar período actual solo si la tabla ya existe
    with engine.connect() as conn:
        tablas = sa.inspect(engine).get_table_names()

        if "reconciliation_results" in tablas:
            conn.execute(
                sa.text("DELETE FROM reconciliation_results WHERE periodo = :p"),
                {"p": periodo_actual}
            )

        if "duplicados_gateway" in tablas:
            conn.execute(
                sa.text("DELETE FROM duplicados_gateway WHERE periodo = :p"),
                {"p": periodo_actual}
            )

        conn.commit()

    # Cargar a SQLite con append
    df_main.to_sql("reconciliation_results", engine,
                   if_exists="append", index=False)
    df_dups.to_sql("duplicados_gateway", engine,
                   if_exists="append", index=False)

    log.info("Período cargado: %s", periodo_actual)
    log.info("reconciliation_results: %d filas", len(df_main))
    log.info("duplicados_gateway: %d filas", len(df_dups))
    log.info("Base de datos actualizada correctamente")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    tabla_path      = os.path.join(DATA_DIR, "reconciliation_output.csv")
    duplicados_path = os.path.join(DATA_DIR, "duplicados_gateway.csv")

    cargar_a_sqlite(tabla_path, duplicados_path)