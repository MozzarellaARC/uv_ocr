# Initialize PaddleOCR instance
def main ():
    from paddleocr import PaddleOCR
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False)

    # Run OCR inference on a sample image 
    result = ocr.predict(
        input="C:\\Users\\M\\Desktop\\hydrant_system\\ref\\Screenshot 2025-09-27 051026.png")

    # Visualize the results and save the JSON results
    for res in result:
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")

def table():
    from paddleocr import TableRecognitionPipelineV2

    pipeline = TableRecognitionPipelineV2()
    ocr = TableRecognitionPipelineV2(use_doc_orientation_classify=True) # 通过 use_doc_orientation_classify 指定是否使用文档方向分类模型
    ocr = TableRecognitionPipelineV2(use_doc_unwarping=True) # 通过 use_doc_unwarping 指定是否使用文本图像矫正模块
    ocr = TableRecognitionPipelineV2(device="gpu") # 通过 device 指定模型推理时使用 GPU
    output = pipeline.predict(input="C:\\Users\\M\\Desktop\\hydrant_system\\ref\\Screenshot 2025-09-27 051026.png")
    for res in output:
        res.print() ## 打印预测的结构化输出
        # res.save_to_img("./output/")
        res.save_to_xlsx("./output/")
        # res.save_to_html("./output/")
        res.save_to_json("./output/")

if __name__ == "__main__":
    main()
    table()