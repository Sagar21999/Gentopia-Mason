from pypdf import PdfReader 
from typing import AnyStr
from gentopia.tools.basetool import *

class PdfReadArgs(BaseModel):
    pdf_file_path: str = Field(..., description="a path to the pdf file")

class PdfRead(BaseTool):
    """Tool that helps to read the contents of a Pdf file."""

    name="pdf_read"
    description=("A tool to read pdf files")
    args_schema: Optional[Type[BaseModel]] = PdfReadArgs

    def _run(self, pdf_file_path: AnyStr) -> str:
        output=[]

        pdf_file = open(pdf_file_path,"rb")

        reader = PdfReader(pdf_file)

        for page in reader.pages:
            pageText = page.extract_text()
            output.append(pageText)

        return '\n\n'.join(output)
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
    

if __name__ == "__main__":
    ans = PdfRead()._run("Attention for transformer")
    print(ans)
