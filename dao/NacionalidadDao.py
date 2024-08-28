from flask import current_app as app
from conexion.Conexion import Conexion

class NacionalidadDao:
    def getNacionalidades(self):

        nacionalidadSQL = """
        SELECT id, descripcion 
        FROM nacionalidades
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(nacionalidadSQL)
            lista_nacionalidades = cur.fetchall()
            return [ { "id": item[0], "descripcion": item[1] } for item in lista_nacionalidades]
        except con.Error as e:
             app.logger.info(e)
        finally:
            cur.close()
            con.close()

