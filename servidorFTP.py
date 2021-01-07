import ftplib
import argparse




# Datos del servidor ftp que por algun motivo no funciona a pesar de ftp.set_pasv(False)
# FTP_HOST = "macbuighome.no-ip.info"
# FTP_USER = "psp"
# FTP_PASS = "265nCwsEzG2Xv6XW"

# Nuevo Servidor ftp; puede variar usuario y contraseña; si eso entrar en la web
# https://dlptest.com/ftp-test/

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "eUj8GeW55SvYaswqUyDSm5v6N"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

# force UTF-8 encoding
ftp.encoding = "utf-8"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", help="Nombre de archivo a subir")
    parser.add_argument("-r", "--ruta", help="Nombre del directorio del servidor donde queremos subir nuestro archivo y Nombre del archivo local a subir",nargs=2)
    parser.add_argument("-b", "--download", help="Nombre de archivo a descargar")
    parser.add_argument("-d", "--directory", help="Crear directorio en servidor FTP")
    parser.add_argument("-c", "--change", help="Cambiar directorio en servidor FTP")
    parser.add_argument("-l", "--dir", help="listar directorios servidor FTP", action="store_const", const=True)


    args = parser.parse_args()
    # list current files & directories
    if args.dir:
        print("listado directorio: ",ftp.pwd())
        ftp.dir()

    # local file name you want to upload
    if args.file:
        if args.change:
            ftp.cwd(args.change)
            print("EL directorio actual:", ftp.pwd())

        print("El nombre de archivo a subir es: ", args.file)
        filename = args.file

        with open(filename, "rb") as fileUp:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {filename}", fileUp)
        print("EL directorio actual:", ftp.pwd())
        ftp.dir()
    # local file name you want to upload
    if args.ruta:

        ftp.cwd(args.ruta[0])
        print("EL directorio actual:", ftp.pwd())

        print("El nombre de archivo a subir es: ", args.ruta[1])
        filename2 = args.ruta[1]

        with open(filename2, "rb") as fileUp:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {filename2}", fileUp)
        print("EL directorio actual:", ftp.pwd())
        ftp.dir()


    # Create directory & list
    if args.directory:
        print("El nombre del directorio a crear es: ", args.directory)
        ftp.mkd(args.directory)
        print("dir para comprobar si se ha creado: ", args.directory)
        ftp.dir()

    # Download file
    if args.download:
        if args.change:
            ftp.cwd(args.change)
            print("EL directorio actual:", ftp.pwd())
        print("El nombre de archivo a procesar es: ", args.download)
        filename = args.download
        with open(filename, "wb") as filedown:
            # use FTP's RETR command to download the file
            ftp.retrbinary(f"RETR {filename}", filedown.write)

    # if args.change:
    #     ftp.cwd(args.change)
    #     print("EL directorio actual:", ftp.pwd())


