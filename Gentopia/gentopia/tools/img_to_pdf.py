import img2pdf
from PIL import Image
from typing import AnyStr
from gentopia.tools.basetool import *

class ImgToPdfArgs(BaseModel):
    img_path: str = Field(..., description="a path to the image")
    pdf_path: str = Field(..., description="a path to the pdf file")


class ImgToPdf(BaseTool):
    """Tool that helps to convert image file .png, .jpg to pdf .pdf file"""

    name="img_to_pdf"
    description=("A tool to convert image to pdf file")
    args_schema: Optional[Type[BaseModel]] = ImgToPdfArgs

    def _run(self, img_path,pdf_path) -> AnyStr:

        try:
            image = Image.open(img_path)
            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdf_path, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()

            return f"succesfully converted image to pdf in {pdf_path}"


        except Exception as e:
            return "Error: " + str(e)
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
    

if __name__ == "__main__":
    ans = ImgToPdf()._run("Attention for transformer")
    print(ans)
