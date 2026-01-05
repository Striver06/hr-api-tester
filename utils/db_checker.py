import psycopg2

def record_exists(query, params, db_cfg):
    conn = psycopg2.connect(**db_cfg)
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchone()
    conn.close()
    return result is not None
