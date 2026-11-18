
from pathlib import Path
from io import BytesIO

from PIL import Image
import cairosvg


# Configurações
PASTA = Path("public/images")
EXTENSOES = {".png", ".jpg", ".jpeg", ".svg"}

QUALIDADE = 85
REMOVER_ORIGINAIS = False

convertidas = 0
erros = 0


def converter_imagem(arquivo):
    destino = arquivo.with_suffix(".webp")

    # Evita sobrescrever arquivos WebP existentes
    if destino.exists():
        print(f"[IGNORADO] {destino} já existe")
        return False

    try:
        if arquivo.suffix.lower() == ".svg":
            # Converte SVG em PNG na memória
            png = cairosvg.svg2png(
                url=str(arquivo),
                scale=2
            )

            imagem = Image.open(BytesIO(png))

        else:
            imagem = Image.open(arquivo)

        with imagem:
            # Preserva transparência
            if imagem.mode not in ("RGB", "RGBA"):
                if "A" in imagem.getbands() or "transparency" in imagem.info:
                    imagem = imagem.convert("RGBA")
                else:
                    imagem = imagem.convert("RGB")

            imagem.save(
                destino,
                format="WEBP",
                quality=QUALIDADE,
                method=6
            )

        print(f"[OK] {arquivo} -> {destino}")

        if REMOVER_ORIGINAIS:
            arquivo.unlink()
            print(f"[REMOVIDO] {arquivo}")

        return True

    except Exception as erro:
        print(f"[ERRO] {arquivo}: {erro}")
        return None


def main():
    global convertidas, erros

    if not PASTA.exists():
        print(f"Pasta não encontrada: {PASTA}")
        return

    arquivos = sorted(
        arquivo
        for arquivo in PASTA.rglob("*")
        if arquivo.is_file()
        and arquivo.suffix.lower() in EXTENSOES
    )

    print(f"Imagens encontradas: {len(arquivos)}\n")

    for arquivo in arquivos:
        resultado = converter_imagem(arquivo)

        if resultado is True:
            convertidas += 1
        elif resultado is None:
            erros += 1

    print("\n" + "=" * 40)
    print("CONVERSÃO FINALIZADA")
    print("=" * 40)
    print(f"Convertidas: {convertidas}")
    print(f"Erros: {erros}")
    print(f"Qualidade: {QUALIDADE}")
    print(f"Remover originais: {REMOVER_ORIGINAIS}")


if __name__ == "__main__":
    main()
