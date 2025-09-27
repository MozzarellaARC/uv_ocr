from argparse import ArgumentParser
from pathlib import Path

from paddleocr import PaddleOCR, TableRecognitionPipelineV2


def run_text_ocr(image_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    result = ocr.predict(input=str(image_path))

    for res in result:
        res.print()
        res.save_to_img(str(output_dir))
        res.save_to_json(str(output_dir))


def run_table_ocr(image_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pipeline = TableRecognitionPipelineV2(
        use_doc_orientation_classify=True,
        use_doc_unwarping=True,
    )

    output = pipeline.predict(input=str(image_path))
    for res in output:
        res.print()
        res.save_to_xlsx(str(output_dir))
        res.save_to_json(str(output_dir))


def _resolve_image_path(path_str: str) -> Path:
    image_path = Path(path_str).expanduser().resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    return image_path


def _parse_image_path(description: str) -> Path:
    parser = ArgumentParser(description=description)
    parser.add_argument("image_path", help="Path to the image file to process.")
    args = parser.parse_args()
    return _resolve_image_path(args.image_path)


def run_text_cli() -> None:
    image_path = _parse_image_path("Run text OCR on an image using PaddleOCR.")
    run_text_ocr(image_path, get_output_dir(image_path))


def run_table_cli() -> None:
    image_path = _parse_image_path("Run table recognition on an image using PaddleOCR.")
    run_table_ocr(image_path, get_output_dir(image_path))


def run_all_cli() -> None:
    image_path = _parse_image_path(
        "Run text OCR and table recognition on an image using PaddleOCR."
    )
    output_dir = get_output_dir(image_path)
    run_text_ocr(image_path, output_dir)
    run_table_ocr(image_path, output_dir)


def get_output_dir(image_path: Path) -> Path:
    return image_path.parent / "output"


if __name__ == "__main__":
    run_text_cli()
    run_table_cli()
    run_all_cli()
