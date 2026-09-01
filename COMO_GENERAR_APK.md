# Cómo generar el APK de OCUPAMOR

Este proyecto ya está preparado para exportarse a Android. Tienes tres caminos;
el **Camino A** es el más fácil y no requiere instalar nada en tu computadora.

---

## Camino A (recomendado): GitHub Actions — el APK se compila solo

1. Sube esta carpeta a un repositorio de GitHub (puede ser el mismo
   `pocket-doom-party`, en una carpeta o en un repo nuevo llamado `ocupamor`).
   Importante: el archivo `buildozer.spec` debe quedar en la **raíz** del repo,
   junto a `main.py`, y la carpeta `.github/workflows/` también debe subirse.
2. En GitHub, entra a la pestaña **Actions**.
3. Elige el flujo **"Construir APK de OCUPAMOR"** y pulsa **Run workflow**.
4. Espera entre 30 y 60 minutos (la primera vez descarga el SDK/NDK de Android).
5. Al terminar, abre la ejecución y descarga el artefacto **ocupamor-apk**.
   Dentro está el archivo `.apk` listo para instalar en el teléfono.

## Camino B: Linux o WSL en tu propia máquina

Buildozer **no funciona en Windows nativo**. En Ubuntu (o WSL2 con Ubuntu):

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool \
  pkg-config zlib1g-dev libncurses5-dev libtinfo6 cmake libffi-dev libssl-dev \
  build-essential ccache
pip install buildozer==1.5.0 cython==0.29.36

cd ocupamor
buildozer -v android debug
```

El APK queda en `bin/ocupamor-1.0-arm64-v8a_armeabi-v7a-debug.apk`.

Para la versión firmada de Play Store: `buildozer android release`.

## Camino C: Google Colab

Sube la carpeta comprimida a Colab y ejecuta los mismos comandos del Camino B
en una celda con `!`. Al final descarga el APK desde `bin/`.

---

## Instalar el APK en el teléfono

1. Copia el `.apk` al teléfono (cable USB, Drive o WhatsApp contigo mismo).
2. En Android: **Ajustes → Seguridad → Instalar apps desconocidas** y habilita
   la app desde la que abrirás el archivo.
3. Toca el `.apk` e instala.

---

## Qué se corrigió para que el APK funcione

- **`buildozer.spec` creado** (antes no existía, sin él no hay APK posible).
  Incluye extensiones `.jpg/.png` y los patrones de `assets/`, de modo que las
  imágenes del abecedario, emociones, señas, figuras y la corneta viajen dentro
  del APK.
- **Dependencias imposibles en Android retiradas del empaquetado**: `pyttsx3` y
  `supabase` no compilan con python-for-android. En el teléfono la voz usa el
  **TextToSpeech nativo de Android** (ya implementado en `speech.py` con
  `pyjnius`), y los datos se guardan localmente.
- **`speech.py`**: en Android ya no intenta lanzar PowerShell/espeak/pyttsx3
  como procesos externos (no existen allí y dejaban la app colgada); si el motor
  nativo no está listo, simplemente no habla.
- **`main.py`**:
  - ya no fuerza una ventana de 400x720 en el teléfono (eso deformaba toda la
    interfaz dentro del APK); el tamaño fijo queda solo para escritorio;
  - el teclado ya no tapa los campos de texto (`softinput_mode`);
  - el **botón "atrás"** de Android navega al menú anterior en vez de cerrar la
    app de golpe;
  - `on_pause`/`on_resume` para que al minimizar no se pierda la sesión;
  - crear la carpeta de imágenes ya no revienta la app cuando el paquete es de
    solo lectura.
- **`requirements.txt`**: marcado como archivo de escritorio, con `pillow`
  añadido y las dependencias de escritorio condicionadas.
- **Workflow de GitHub Actions** para compilar el APK en la nube sin instalar
  nada.
