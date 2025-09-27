# UV OCR

Command line utility built on top of [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for running both text OCR and table structure recognition on a single image.

## Prerequisites

- Python 3.9 or newer.
- All Python dependencies from `requirements.txt` installed (for example: `pip install -r requirements.txt`).
- PaddleOCR downloads required model weights on first run; make sure the machine has internet access for the initial execution.

## Usage

Run text OCR only:

```powershell
uv run ocr C:\path\to\your\image.png
```

Run table recognition only:

```powershell
uv run ocr-table C:\path\to\your\image.png
```

Run both pipelines in a single pass:

```powershell
uv run ocr-all C:\path\to\your\image.png
```

Each command will:

- Print the structured predictions to the console.
- Save the generated image/JSON/XLSX outputs inside an `output` subdirectory that lives alongside your source image.

If the provided path does not exist, the tool will exit with an error.

## Output

`PaddleOCR` will create files such as `ocr_vis.png`, `ocr_result.json`, and table exports (for example `table.xlsx`) inside `<image directory>/output/`. File names may vary depending on the PaddleOCR version. Each invocation writes into the `output` folder next to the image you provided, letting you keep results grouped per source image.

## Notes

- When running table recognition, GPU acceleration is optional. The current configuration uses CPU execution by default. Consult the PaddleOCR documentation if you want to fine-tune device settings.
- The tool does not recursively process multiple files; run it once per image to keep the outputs organized.
