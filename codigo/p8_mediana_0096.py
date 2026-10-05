# Samuel Martinez NC 0096
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/condorito.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("condorito0096.jpg", imagen)
cv2.imshow("condorito_filtrado.jpg ", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultado/condorito_filtrado.jpg",
    imagen_filtrada
)
cv2.imwrite(
    "resultado/condorito0096.jpg",
    imagen
)


print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultado/condorito_filtrado.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()