#faz a conexão e operações relacionadas ao banco
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = psycopg.connect( #conecte meu python a este postgreSQL
        host="localhost",
        port=5432,
        dbname="studypath",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )

    return conexao

def buscar_estudos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            estudos.id,
            materias.nome AS materia,
            estudos.assunto,
            estudos.data,
            estudos.horas
        FROM estudos
        JOIN materias
            ON estudos.materia_id = materias.id
    """)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados

def buscar_materia(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM materias WHERE nome = %s",
        (nome,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


def inserir_estudo(materia_id, assunto, data, horas):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO estudos (materia_id, assunto, data, horas)
        VALUES (%s, %s, %s, %s)
    """, (materia_id, assunto, data, horas))

    conexao.commit()

    cursor.close()
    conexao.close()

def editar_estudo(id_estudo, materia_id, assunto, data, horas):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE estudos
        SET materia_id = %s,
            assunto = %s,
            data = %s,
            horas = %s
        WHERE id = %s
    """, (materia_id, assunto, data, horas, id_estudo))

    conexao.commit()

    cursor.close()
    conexao.close()

def editar_estudo_banco(id_estudo, materia_id, assunto, data, horas):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE estudos
        SET materia_id = %s,
            assunto = %s,
            data = %s,
            horas = %s
        WHERE id = %s
    """, (materia_id, assunto, data, horas, id_estudo))

    conexao.commit()

    cursor.close()
    conexao.close()


def remover_estudo(id_estudo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM estudos WHERE id = %s",
        (id_estudo,)
    )

    conexao.commit()

    cursor.close()
    conexao.close()